import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.metrics import accuracy_score, classification_report
data = pd.read_csv("https://raw.githubusercontent.com/justmarkham/pycon-2016-tutorial/master/data/sms.tsv", sep='\t', names=["label", "message"])

data['label_num'] = data.label.map({'ham': 0, 'spam': 1})
X = data['message']
y = data['label_num']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)


vectorizer = CountVectorizer()
X_train_vec = vectorizer.fit_transform(X_train)
X_test_vec = vectorizer.transform(X_test)


model = MultinomialNB()
model.fit(X_train_vec, y_train)

y_pred = model.predict(X_test_vec)


accuracy = accuracy_score(y_test, y_pred)
print("Accuracy:", accuracy)
print("\nClassification Report:\n", classification_report(y_test, y_pred))

def predict_message(msg):
    msg_vec = vectorizer.transform([msg])
    result = model.predict(msg_vec)
    return "Spam" if result[0] == 1 else "Not Spam"

# Test
print("\nTest Message: 'Congratulations, you've won a prize! Call now'")
print("Prediction:", predict_message("Congratulations, you've won a prize! Call now"))
