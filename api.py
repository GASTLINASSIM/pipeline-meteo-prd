import os
import sqlite3
from datetime import datetime
from typing import Dict, Any, Optional

import numpy as np
import pandas as pd
import joblib
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field

DB_PATH = r"C:\Users\nassi\OneDrive - Groupe INSEEC (POCE)\Bureau\ECE - M2\Mastering Data Life Cycle - Mme BENNAI Soufia\Projet\data\pipeline.db"
MODEL_PATH = r"models/temperature_t_plus_1_model.joblib"
FEATURES = ['temperature_2m', 'relative_humidity_2m', 'precipitation', 'pressure_msl', 'wind_speed_10m', 'cloud_cover', 'hour', 'dayofweek', 'month', 'hour_sin', 'hour_cos', 'dow_sin', 'dow_cos', 'month_sin', 'month_cos', 'temperature_2m_lag_1', 'temperature_2m_lag_2', 'temperature_2m_lag_3', 'temperature_2m_roll_mean_3', 'temperature_2m_roll_mean_6', 'temperature_2m_roll_std_6', 'is_hot', 'is_raining', 'strong_wind']

app = FastAPI(title="Meteo Forecast API", version="1.0")
_model = None

def _load_model():
    global _model
    if _model is None:
        if not os.path.exists(MODEL_PATH):
            raise FileNotFoundError(f"Model not found: {MODEL_PATH}")
        _model = joblib.load(MODEL_PATH)
    return _model

class PredictRequest(BaseModel):
    features: Dict[str, float] = Field(..., description="Feature dict at time t")
    source_time: Optional[str] = Field(default=None, description="Timestamp string for the row (primary key)")

class PredictResponse(BaseModel):
    created_at: str
    y_pred: float
    source_time: Optional[str] = None

PredictRequest.model_rebuild()
PredictResponse.model_rebuild()

@app.get("/health")
def health() -> Dict[str, Any]:
    # charge le modèle à la demande pour refléter l'état réel
    try:
        _load_model()
        model_loaded = True
    except Exception:
        model_loaded = False

    return {
        "status": "ok",
        "model_loaded": model_loaded,
        "n_features_expected": len(FEATURES),
        "db_path_exists": os.path.exists(DB_PATH),
        "model_path_exists": os.path.exists(MODEL_PATH),
    }

@app.post("/predict", response_model=PredictResponse)
def predict(req: PredictRequest) -> PredictResponse:
    model = _load_model()

    missing = [f for f in FEATURES if f not in req.features]
    if missing:
        raise HTTPException(status_code=400, detail=f"Missing features: {missing}")

    # DataFrame => pas de warning sklearn + feature names respectés
    x_df = pd.DataFrame([[float(req.features[f]) for f in FEATURES]], columns=FEATURES)
    y_pred = float(model.predict(x_df)[0])
    created_at = datetime.utcnow().isoformat()

    # Log DB selon TON schéma réel: predictions(time TEXT PK, y_true, y_pred, error)
    if req.source_time is None:
        raise HTTPException(status_code=400, detail="source_time is required because predictions.time is the primary key")

    with sqlite3.connect(DB_PATH) as conn:
        conn.execute(
            "INSERT OR REPLACE INTO predictions(time, y_true, y_pred, error) VALUES (?, ?, ?, ?)",
            (req.source_time, None, y_pred, None),
        )
        conn.commit()

    return PredictResponse(created_at=created_at, y_pred=y_pred, source_time=req.source_time)