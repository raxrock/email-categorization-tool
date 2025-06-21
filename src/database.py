# src/database.py
import sqlite3
import pandas as pd

def save_to_db(df, db='email_data.db'):
    conn = sqlite3.connect(db)
    df.to_sql('emails', conn, if_exists='append', index=False)
    conn.close()