import sys
import os
# Check if the model exists before running the main script
if not os.path.exists('models/classifier.pkl'):
    raise FileNotFoundError("❌ Model not found. Please train the model first using labeled data.")

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from src.gmail_connect import authenticate, fetch_emails
from src.model import predict_category
from src.database import save_to_db
import pandas as pd

service = authenticate()
emails = fetch_emails(service, max_results=20)

# Predict categories
for email in emails:
    text = email['subject'] + " " + email['body']
    email['category'] = predict_category(text)

df = pd.DataFrame(emails)
save_to_db(df)
df.to_csv('data/emails.csv', index=False)
print("Categorized and saved!")