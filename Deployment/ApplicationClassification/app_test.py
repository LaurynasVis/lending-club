import random
from locust import HttpUser, task, constant_throughput

test_applications = [
    {
        "loan_title": "Debt consolidation",
        "amount_requested": 10000.0,
        "risk_score": 600.0,
        "employment_length": "5 years",
        "debt_to_income_ratio": 10.0,
    },
    {
        "loan_title": "Debt consolidation",
        "amount_requested": 5000.0,
        "risk_score": 700.0,
        "employment_length": "9 years",
        "debt_to_income_ratio": 5.0,
    },
]


class BankLoan(HttpUser):
    wait_time = constant_throughput(1)

    @task
    def predict(self):
        self.client.post(
            "/predict",
            json=random.choice(test_applications),
            timeout=1,
        )