import random
from locust import HttpUser, task, constant_throughput

test_applications = [
    {
        "amount_requested": 8000.0,
        "purpose": "Debt consolidation",
        "term": 36.0,
        "installment": 256.97,
        "fico_range_low": 720.0,
        "bc_open_to_buy": 791.0,
        "all_util": 28.0,
        "emp_title": "Manager",
    },
    {
        "amount_requested": 8000.0,
        "purpose": "Debt consolidation",
        "term": 36.0,
        "installment": 256.97,
        "fico_range_low": 720.0,
        "bc_open_to_buy": 791.0,
        "all_util": 28.0,
        "emp_title": "Manager",  
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
