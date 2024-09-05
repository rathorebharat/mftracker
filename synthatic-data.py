import pandas as pd
from faker import Faker
import random
from datetime import datetime, timedelta

# Initialize Faker
fake = Faker()

# Number of records you want to generate
num_records = 100

# Helper function to generate random timestamps
def random_timestamp(start_date):
    return start_date + timedelta(days=random.randint(0, 365))

# Generate synthetic data
data = {
    "id": [fake.uuid4() for _ in range(num_records)],
    "title": [fake.word() for _ in range(num_records)],
    "vendor": [fake.company() for _ in range(num_records)],
    "product_type": [fake.word() for _ in range(num_records)],
    "created_at": [random_timestamp(datetime(2023, 1, 1)).isoformat() for _ in range(num_records)],
    "updated_at": [random_timestamp(datetime(2023, 6, 1)).isoformat() for _ in range(num_records)],
    "published_at": [random_timestamp(datetime(2023, 7, 1)).isoformat() for _ in range(num_records)],
    "tags": [",".join(fake.words(nb=3)) for _ in range(num_records)],
    "variants": [random.randint(1, 10) for _ in range(num_records)]
    # Add more fields as required by the schema
}

# Convert to DataFrame
df = pd.DataFrame(data)

# Export to CSV
df.to_csv("synthetic_shopify_products.csv", index=False)

print("Synthetic CSV file generated successfully.")
