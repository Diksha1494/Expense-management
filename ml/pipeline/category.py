import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB
import pickle


data = pd.read_csv("transactions.csv")   # columns: description, category


X = data['Description']
y = data['Category']


vectorizer = TfidfVectorizer()
X_vec = vectorizer.fit_transform(X)


model = MultinomialNB()
model.fit(X_vec, y)


with open("expense_model.pkl", "wb") as f:
    pickle.dump((vectorizer, model), f)

print("Model trained & saved as expense_model.pkl")
