from locust import HttpUser, task, between
import csv
import random

class EcommerceUser(HttpUser):
    wait_time = between(1, 3)
    
    def on_start(self):
        # Load product data
        with open("data/products.csv") as f:
            self.products = list(csv.DictReader(f))
    
    @task(3)
    def browse_products(self):
        product = random.choice(self.products)
        self.client.get(f"/products/{product['product_id']}")
    
    @task(1)
    def purchase_product(self):
        product = random.choice(self.products)
        self.client.post(
            "/cart",
            json={
                "product_id": product["product_id"],
                "quantity": 1
            }
        )
        self.client.post("/checkout")
