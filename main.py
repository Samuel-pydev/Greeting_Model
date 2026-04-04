from dataset import sentences, labels
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
import joblib as jb

vectorizer = TfidfVectorizer() # 

#   reads all sentences and builds a vocabulary then converts each sentence to rows of numbers based on the vocabulary
X = vectorizer.fit_transform(sentences) 

#   Splitting the dataset for training and testing
X_train, X_test, y_train, y_test = train_test_split(
    X, labels, test_size=0.2, random_state=42
)

model = LogisticRegression()
model.fit(X_train, y_train)
print("\nModel Trained ✔\n")

#   Getting Accuracy score of the trained model
score = model.score(X_test, y_test)
print("Accuracy: ", score*100,"%")

# Saving model and vectorizer 
jb.dump(model, "MDL.pkl")
jb.dump(vectorizer, "VTR.pkl")

print("Saved ✅")

