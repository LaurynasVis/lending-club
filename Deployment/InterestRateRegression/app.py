import pickle
import pandas as pd
from pydantic import BaseModel

from fastapi import FastAPI


# Pydantic classes for input and output
class LoanInterestRate(BaseModel):
    installment: float
    term: float
    amount_requested: float
    fico_range_low: float
    bc_open_to_buy: float
    purpose: str
    annual_inc: float
    debt_to_income_ratio: float

class PredictionOut(BaseModel):
    interest_rate: float


# Load the model
model = pickle.load(open("interest_rate_model-0.1.0.pkl", "rb"))

# Start the app
app = FastAPI()


# Home page
@app.get("/")
def home():
    return {"message": "Loan interest rate prediction", "model_version": 0.1}


# Inference endpoint
@app.post("/predict", response_model=PredictionOut)
def predict(payload: LoanInterestRate):
    cust_df = pd.DataFrame([payload.model_dump()])
    preds = model.predict(cust_df)
    result = {"interest_rate": preds}
    return result
