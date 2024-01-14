import pickle
import pandas as pd
from pydantic import BaseModel

from fastapi import FastAPI


# Pydantic classes for input and output
class LoanApplication(BaseModel):
    loan_title: str
    amount_requested: float
    risk_score: float
    employment_length: str
    debt_to_income_ratio: float

class PredictionOut(BaseModel):
    request_status: str

# Load the model
model = pickle.load(open('application_model-0.1.0.pkl', 'rb'))

# Start the app
app = FastAPI()

# Home page
@app.get("/")
def home():
    return {"message": "Loan application classification", "model_version": 0.1}

# Inference endpoint
@app.post("/predict", response_model=PredictionOut)
def predict(payload: LoanApplication):
    cust_df = pd.DataFrame([payload.model_dump()])
    preds = model.predict_proba(cust_df)[0,1]
    if preds > 0.5:
        preds = "Accepted"
    else:
        preds = "Rejected"
    result = {"request_status": preds}
    return result
