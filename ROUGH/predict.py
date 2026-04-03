import joblib

# Load the pair
model = joblib.load("model.pkl")
vectorizer = joblib.load("vectorizer.pkl")

# testing 
sentence = [" wtf "]
X = vectorizer.transform(sentence)
prediction = model.predict(X)

print(" Grettings " if prediction[0] == 1 else " What the freak ?  " )