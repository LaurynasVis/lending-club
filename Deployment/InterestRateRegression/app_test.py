import random
from locust import HttpUser, task, constant_throughput

test_applications = [
    {
        "installment": 194.02,
        "term": 36,
        "amount_requested": 10000.0,
        "fico_range_low": 750.0,
        "bc_open_to_buy": 7599.0,
        "purpose": "Debt consolidation",
        "annual_inc": 60000.0,
        "debt_to_income_ratio": 14.92,
    },
    {
        "installment": 194.02,
        "term": 36,
        "amount_requested": 10000.0,
        "fico_range_low": 750.0,
        "bc_open_to_buy": 7599.0,
        "purpose": "Debt consolidation",
        "annual_inc": 60000.0,
        "debt_to_income_ratio": 14.92,
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
