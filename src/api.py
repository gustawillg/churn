from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import joblib
import numpy as np

app = FastAPI()

model = joblib.load("modelo_churn.pkl")

class PredictionInput(BaseModel):
    features: list

@app.post("/predict")
def predict(input_data: PredictionInput):
    try:
        data = np.array(input_data.features).reshape(1, -1)
        prediction = model.predict(data)
        return {"prediction": int(prediction[0])}
    except Exception as e: 
        raise HTTPException(status_code=400, detail=str(e))