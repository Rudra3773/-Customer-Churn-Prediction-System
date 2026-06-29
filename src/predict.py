import joblib
import pandas as pd
import os


def load_model():

    model_path = os.path.abspath(
        os.path.join(
            os.path.dirname(__file__),
            "..",
            "models",
            "churn_model.pkl"
        )
    )

    model = joblib.load(model_path)

    return model


def predict_churn(input_data):
    
    model = load_model()

    input_df = pd.DataFrame([input_data])

    prediction = model.predict(input_df)[0]

    probability = model.predict_proba(input_df)[0][1]

    return prediction, probability