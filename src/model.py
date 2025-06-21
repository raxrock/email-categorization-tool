# src/model.py
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB
import pickle

def train_model(df):
    df['content'] = df['subject'] + " " + df['body']
    from src.preprocess import clean_text
    df['content'] = df['content'].apply(clean_text)

    vectorizer = TfidfVectorizer(max_features=1000)
    X = vectorizer.fit_transform(df['content'])
    y = df['category']  # Assumes you label manually

    clf = MultinomialNB()
    clf.fit(X, y)

    # Save model and vectorizer
    pickle.dump(clf, open('models/classifier.pkl', 'wb'))
    pickle.dump(vectorizer, open('models/vectorizer.pkl', 'wb'))

def predict_category(text):
    from src.preprocess import clean_text
    clf = pickle.load(open('models/classifier.pkl', 'rb'))
    vectorizer = pickle.load(open('models/vectorizer.pkl', 'rb'))
    cleaned = clean_text(text)
    return clf.predict(vectorizer.transform([cleaned]))[0]