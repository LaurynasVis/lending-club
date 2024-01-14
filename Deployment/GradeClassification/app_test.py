import random
from locust import HttpUser, task, constant_throughput

test_applications = [
    {
        "installment": 300.0,
        "term": 36.0,
        "amount_requested": 10000.0,
        "mths_since_rcnt_il": 4.0,
        "all_util": 28.0,
        "open_acc_6m": 1.0,
        "purpose": "Debt consolidation",
        "fico_range_low": 720.0,
        "emp_title": "Manager",
    },
    {
       "installment": 300.0,
        "term": 36.0,
        "amount_requested": 10000.0,
        "mths_since_rcnt_il": 4.0,
        "all_util": 28.0,
        "open_acc_6m": 1.0,
        "purpose": "Debt consolidation",
        "fico_range_low": 720.0,
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
