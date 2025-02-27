from locust import HttpUser, task, between
import csv
import random
import logging

logging.basicConfig(level=logging.INFO)

class EcommerceUser(HttpUser):
    wait_time = between(1, 3)
    
    def on_start(self):
        # Load product data
        try:
           with open("data/products.csv") as f:
            self.products = list(csv.DictReader(f))
            logging.info("Loaded product data.")
        except FileNotFoundError:
            self.products = []
            logging.error("Product data file not found.")
        except Exception as e:
            self.products = []
            logging.error(f"An error occurred: {e}")
        
            
    
    @task(3)
    def browse_products(self):
        if not self.products:
            return
        product = random.choice(self.products)
        self.client.get(f"/products/{product['product_id']}")
        logging.info(f"Browsed product {product['product_id']}")

    @task(1)
    def purchase_product(self):
        if not self.products:
            return
        product = random.choice(self.products)
        self.client.post(
            "/cart",
            json={
                "product_id": product["product_id"],
                "quantity": 1
            }
        )
        self.client.post("/checkout")
        logging.info(f"Purchased product {product['product_id']}")
