import joblib

# Load the model and vectorizer
model = joblib.load("MD.pkl")
vectorizer = joblib.load("VTR.pkl")

print("\n","#~#~"*20, "Greeting Model - Type quit to Quit ", "#~#~"*20)

while True:
    user_input = input("\n🧍‍♂️: ")

    if user_input.lower() == 'quit':
        print("\n🖥: Bye")
        break
    
    # Turning user_input in to vocabulary that would be use use to convert to text 
    X = vectorizer.transform([user_input])

    prediction = model.predict(X)

    if prediction[0] == 1:
        print("\n🖥: Greetings")
    else:
        print("\n🖥: No - Greetings")