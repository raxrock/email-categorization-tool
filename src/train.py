import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from src.model import train_model

import pandas as pd
from src.model import train_model

# Load labeled training data
df = pd.read_csv('data/emails_labeled.csv')

# Train model and save to models/
train_model(df)

print("✅ Model trained and saved.")