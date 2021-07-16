from joblib import load
import pandas as pd


def detect_sentiment(text):
    model = load('modeling/models/svm_model.joblib')
    df = pd.DataFrame([text])
    prediction = model.predict(df[0])

    return prediction[0]




