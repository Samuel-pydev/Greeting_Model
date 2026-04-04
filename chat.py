import joblib
import random
from dataset import responses

# Load the model and vectorizer
model = joblib.load("MDL.pkl")
vectorizer = joblib.load("VTR.pkl")

print("\n","#~#~"*5, "Greeting Model - Type quit to Quit ", "#~#~"*5)

while True:
    user_input = input("\n🧍‍♂️: ")

    if user_input.lower() == 'quit':
        print("\n🖥: Bye")
        break
    
    # Turning user_input in to vocabulary that would be use use to convert to text 
    X = vectorizer.transform([user_input])

    prediction = model.predict(X)

    intent = str(prediction[0])
    reply = random.choice(responses[intent])
    print("\n🖥: ", reply, )
