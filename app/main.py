from fastapi import FastAPI
from pydantic import BaseModel
import pickle
from typing import List

app = FastAPI(title="Churn Scoring API")

with open("model.pkl", "rb") as f:
    model = pickle.load(f)

class CustomerFeatures(BaseModel):
    recencydays: float
    frequency180d: int
    monetary180d: float
    sessions30d: int
    lastvisitdaysago: int

@app.get("/health")
def health():
    return {"status": "ok"}

@app.post("/predict")
def predict(data: CustomerFeatures):
    X = [[
        data.recencydays,
        data.frequency180d,
        data.monetary180d,
        data.sessions30d,
        data.lastvisitdaysago
    ]]
    prob = model.predict_proba(X)[0][1]
    pred = int(prob >= 0.5)
    risk = "high" if prob >= 0.7 else "medium" if prob >= 0.4 else "low"

    if risk == "high":
        risk_explanation = "High churn risk due to recent activity and purchase patterns"
    elif risk == "medium":
        risk_explanation = "Moderate churn risk with mixed engagement signals"
    else:
        risk_explanation = "Low churn risk based on recent engagement and spend"

    return {
        "churn_probability": round(prob, 4),
        "predicted_class": pred,
        "risk_level": risk,
        "risk_explanation": risk_explanation
    }

@app.post("/batch_predict")
def batch_predict(data: List[CustomerFeatures]):
    results = []

    for d in data:
        X = [[
            d.recencydays,
            d.frequency180d,
            d.monetary180d,
            d.sessions30d,
            d.lastvisitdaysago
        ]]
        prob = model.predict_proba(X)[0][1]
        pred = int(prob >= 0.5)
        risk = "high" if prob >= 0.7 else "medium" if prob >= 0.4 else "low"

        results.append({
            "churn_probability": round(prob, 4),
            "predicted_class": pred,
            "risk_level": risk
        })

    return results