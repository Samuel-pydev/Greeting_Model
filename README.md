# Greetings Classifier

A text classification model that detects whether a sentence is a greeting or not. Built from scratch using Python and scikit-learn — no tutorials copied, no code dumped in blindly.

---

## What It Does

You give it a sentence. It tells you if it's a greeting or not.

```
You: wagwan
Model: That's a greeting

You: how much does it cost
Model: Not a greeting
```

---

## How It Works

The pipeline has three steps:

1. **Vectorization** — Converts raw text into numbers using TF-IDF. Words that are rare but meaningful get weighted higher than common words that appear everywhere.

2. **Training** — A Logistic Regression model learns the difference between greetings and non-greetings from 200 labeled examples (100 of each).

3. **Prediction** — New sentences are transformed using the same vocabulary and passed through the trained model.

---

## Project Structure

```
greetings-model/
├── MAIN
├   ├── dataset.py      # Dataset
├   ├── main.py         # vectorization, training, and saving
├   ├── chat.py         # Interactive input loop
├── ROUGH # rough part        
├   ├── data.py         # Dataset, vectorization, training, and saving
├   ├── chat.py         # Interactive input loop
├   ├── predict.py      # To predict user's text
```

---

## Stack

- Python 3
- scikit-learn — TfidfVectorizer, LogisticRegression, train_test_split
- joblib — saving and loading the model and vectorizer

---

## Setup

```bash
pip install -r requirements.txt
```

Train the model:

```bash
python data.py
```

Run the interactive chat:

```bash
python chat.py
```

---

## Dataset

200 manually labeled sentences — 100 greetings, 100 non-greetings. Greetings include standard English phrases as well as informal and slang variations like "wagwan", "wsg", "howfar", and "wazzup". Non-greetings cover questions, requests, and statements across different topics.

Balanced classes were intentional — an imbalanced dataset caused the model to default to predicting "greeting" for almost everything, inflating accuracy artificially.

---

## Accuracy

**75%** on a 20% test split with 200 balanced samples.

Earlier runs hit 83-90% but those numbers were misleading — the dataset was heavily skewed toward greetings so the model learned to default to 1. After balancing to 100/100, accuracy dropped to an honest 75%.

---

## Known Limitations

- **No negation understanding** — "hey that's not good" gets classified as a greeting because the model sees "hey" and "good" independently. It has no concept of "not" flipping meaning.
- **Vocabulary dependent** — words never seen during training have no signal and get swept toward the majority class.
- **Small dataset** — 200 examples is enough to learn basic patterns but real world robustness needs more data and variety.

These are limitations of bag-of-words approaches in general. The next step up is embeddings, which capture context and meaning rather than just word presence.

