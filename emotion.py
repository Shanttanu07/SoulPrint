import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.svm import SVC  # Import Support Vector Classification
from sklearn.metrics import classification_report

# 1. Load the Data
data = pd.read_csv("tweet_emotions.csv")

# 2. Text Preprocessing
data['content'] = data['content'].str.lower().str.replace('[^\w\s]', '') 

# 3. Splitting the Data
X_train, X_test, y_train, y_test = train_test_split(data['content'], data['sentiment'], test_size=0.2, random_state=42)

# 4. Vectorization
vectorizer = TfidfVectorizer(stop_words='english', max_features=5000)
X_train_vec = vectorizer.fit_transform(X_train)
X_test_vec = vectorizer.transform(X_test)

# 5. Model Building
model = SVC(kernel='linear')  # Using a linear kernel for the SVM. You can adjust this as needed.

# 6. Training
model.fit(X_train_vec, y_train)

# 7. Evaluation
y_pred = model.predict(X_test_vec)
print(classification_report(y_test, y_pred))

# 8. Prediction



def predict(new_data):
    new_data_vec = vectorizer.transform(new_data)
    predicted_sentiments = model.predict(new_data_vec)
    return predicted_sentiments[0]

