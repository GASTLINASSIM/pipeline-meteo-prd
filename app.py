
from fastapi import FastAPI
from pydantic import BaseModel
import joblib
import pandas as pd

MODEL_PATH = "models/temperature_t_plus_1_model.joblib"
model = joblib.load(MODEL_PATH)

class PredictRequest(BaseModel):
    features: dict

app = FastAPI(title="Temperature t+1 Prediction API")

@app.get("/health")
def health():
    return {"status": "ok"}

@app.post("/predict")
def predict(req: PredictRequest):
    # Les features doivent correspondre aux colonnes d'entraînement
    X = pd.DataFrame([req.features])
    pred = float(model.predict(X)[0])
    return {"prediction_t_plus_1": pred}
