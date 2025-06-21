# 📬 Email Categorization Tool

A complete end-to-end Python application that connects to your Gmail account, fetches your emails via the Gmail API, applies natural language processing (NLP) to the email content, and classifies them into predefined categories like Work, Personal, Promotions, Finance, Travel, and more. The tool outputs data suitable for visualization in tools like Tableau or Google Looker Studio.

---

## 🚀 Features

- ✅ Gmail API OAuth2.0 authentication
- 📥 Automatic fetching of emails (subject + body)
- 🧹 Preprocessing using NLTK (tokenization, stopword removal)
- 🧠 Machine learning model (Naive Bayes classifier with TF-IDF)
- 🗃️ Stores categorized results in CSV and SQLite database
- 📊 Ready for visualization in Tableau, Excel, or Google Sheets
- 🛡️ Secured using `.gitignore` for sensitive info

---

## 🗂️ Project Structure

```
email-categorization-tool/
├── src/
│   ├── main.py             # Entry point to fetch and classify emails
│   ├── gmail_connect.py    # Handles Gmail API authentication and fetch
│   ├── preprocess.py       # Cleans and preprocesses email content
│   ├── model.py            # ML model training and prediction
│   ├── database.py         # Stores results in SQLite
│   └── __init__.py
├── models/                 # Trained model artifacts (.pkl files)
├── data/                   # Labeled data and prediction results
├── notebooks/              # Jupyter notebooks (optional)
├── train.py                # Script to train model using labeled data
├── requirements.txt        # All Python dependencies
├── .gitignore              # Prevents sensitive files from being committed
├── README.md               # Project documentation
└── run.sh                  # Optional shell script to execute project
```

---

## 🔐 Setup Instructions

### 1. Clone the Repository

```bash
git clone https://github.com/YOUR_USERNAME/email-categorization-tool.git
cd email-categorization-tool
```

### 2. Create a Virtual Environment

```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Gmail API Setup

- Create a Google Cloud project → OAuth credentials.
- Download `credentials.json` and place it in the project root.
- Add yourself as a test user in OAuth settings.

---

## 🧪 How to Use

### ▶️ Train the Model (Only Once)

```bash
python src/train.py
```

This uses `data/emails_labeled.csv` to train the classifier and saves it in `models/`.

### ▶️ Classify Emails

```bash
python src/main.py
```

This:
- Authenticates with Gmail
- Fetches email subject & body
- Predicts categories using the trained model
- Saves output to `data/emails.csv` and `email_data.db`

---

## 📊 Visualization Options

- **Tableau**: Load `data/emails.csv` and create dashboards.
- **Looker Studio**: Import Google Sheets version of the CSV.
- **Excel or Pandas**: Analyze and filter directly.

---

## 📁 Sample Categories

- Work
- Personal
- Promotions
- Finance
- Travel
- Job Boards
- Education
- Government
- Insurance
- 250+ total categories (auto-generated)

---

## 📌 Important Notes

- Do **NOT** commit your `credentials.json` or `token.json`.
- `.gitignore` is already configured to exclude:
  - Auth tokens
  - Models
  - Large data files
  - Cache and logs

---

## 🧠 Future Improvements

- Web dashboard using Flask or FastAPI
- Scheduled email pulls (via cron or APScheduler)
- Integration with Google Sheets API
- Cloud deployment (GCP, AWS Lambda)

---

## 👨‍💻 Author

**Rakshith KK**  
Built with 💡, Python, and a lot of patience

---

## 📄 License

This project is open-source and available under the [MIT License](LICENSE).