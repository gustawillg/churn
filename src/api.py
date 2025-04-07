from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import joblib
import numpy as np

app = FastAPI()

model = joblib.load("modelo_churn.pkl")

expected_features = model.n_features_in_

class PredictionInput(BaseModel):
    features: list

@app.post("/predict")
def predict(input_data: PredictionInput):
    if len(input_data.features) != expected_features:
        raise HTTPException(
            status_code=400,
            detail=f"Esperado {expected_features} features, mas recebeu {len(input_data.features)}."
        )
    try:
        data = np.array(input_data.features).reshape(1, -1)
        prediction = model.predict(data)
        return {
            "prediction": int(prediction[0]),
            "message": "Risco alto de perda do cliente." if prediction[0] == 1 else "Risco baixo de perda do cliente."
        }
    except Exception as e: 
        raise HTTPException(status_code=400, detail=str(e))
