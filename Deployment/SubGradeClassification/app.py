import pickle
import pandas as pd
from pydantic import BaseModel

from fastapi import FastAPI


# Pydantic classes for input and output
class LoanSubgrade(BaseModel):
    installment: float
    term: float
    amount_requested: float
    all_util: float
    purpose: str
    fico_range_low: float
    emp_title: str
    bc_open_to_buy: float

class PredictionOut(BaseModel):
    subgrade: str


# Load the model
model = pickle.load(open("subgrade_model-0.1.0.pkl", "rb"))

# Start the app
app = FastAPI()


# Home page
@app.get("/")
def home():
    return {"message": "Loan subgrade classification", "model_version": 0.1}


# Inference endpoint
@app.post("/predict", response_model=PredictionOut)
def predict(payload: LoanSubgrade):
    cust_df = pd.DataFrame([payload.model_dump()])
    preds = model.predict(cust_df)
    result = {"subgrade": preds}
    return result
