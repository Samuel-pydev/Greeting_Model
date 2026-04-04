import joblib
import random

# Load the pair
model = joblib.load("model.pkl")
vectorizer = joblib.load("vectorizer.pkl")

print( " Greet, type 'q' to exit. \n  " )

while True : 
    user_input = input("You: ")

    if user_input.lower() == 'quit':
        print(" Bye ")
        break

    X = vectorizer.transform([user_input])
    prediction = model.predict(X)


    
    if prediction[0] == 1:
        print(" Model: Greetings Earthlings. \n ")
        print(prediction[0])
    else:
        print("Model: Wah da freak ? ")