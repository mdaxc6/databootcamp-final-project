from joblib import load
import pandas as pd

model = load('../../modeling/models/svm_model.joblib')


def detect_sentiment(text):
    df = pd.DataFrame([text])
    prediction = model.predict(df[0])

    return prediction[0]



print(detect_sentiment("This movie was pretty good."))