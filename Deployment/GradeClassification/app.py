import pickle
import pandas as pd
from pydantic import BaseModel

from fastapi import FastAPI


# Pydantic classes for input and output
class LoanGrade(BaseModel):
    installment: float
    term: float
    amount_requested: float
    mths_since_rcnt_il: float
    all_util: float
    open_acc_6m: float
    purpose: str
    fico_range_low: float
    emp_title: str

class PredictionOut(BaseModel):
    grade: str


# Load the model
model = pickle.load(open("grade_model-0.1.0.pkl", "rb"))

# Start the app
app = FastAPI()


# Home page
@app.get("/")
def home():
    return {"message": "Loan grade classification", "model_version": 0.1}


# Inference endpoint
@app.post("/predict", response_model=PredictionOut)
def predict(payload: LoanGrade):
    cust_df = pd.DataFrame([payload.model_dump()])
    preds = model.predict(cust_df)
    result = {"grade": preds}
    return result
