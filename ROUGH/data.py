



from sklearn.feature_extraction.text import TfidfVectorizer , CountVectorizer

vectorizer = TfidfVectorizer()

""" 
fit_transform divided into two steps 

fit = reads all of sentences and builds a vocabulary ,
transform = it converts each sentences into a row of numbers based on that vocabulary

"""
X = vectorizer.fit_transform(sentences)

print(X.shape)

from sklearn.model_selection import train_test_split

X_train, X_test, y_train, y_test = train_test_split(
    X, labels, test_size=0.2 , random_state=42
)

print( X_train.shape, X_test.shape )

from sklearn.linear_model import LogisticRegression # Classification Algo

model = LogisticRegression()
model.fit(X_train, y_train)

print(" Model trained... ")

# test_sentence = [" update "]

# X_new = vectorizer.transform(test_sentence) # to convert sentences to numbers
# prediction = model.predict(X_new)
# print("\n => ",prediction)

score = model.score(X_test, y_test)
print("Accuracy: ", score)

import joblib as jb  # saved the model and other things recommended by sklearn

jb.dump(model, "model.pkl")
jb.dump(vectorizer, "vectorizer.pkl")

print("Saved")

# print (labels)
# print (len(sentences), len(labels))
# for i in range(len(sentences)):
#     print(i, sentences[i], "->", labels[i])

# print(model.classes_)
# print(model.predict_proba(vectorizer.transform(["hello"])))