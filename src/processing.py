import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder


def load_data(filepath):
    """
    Load dataset
    """
    df = pd.read_csv(filepath)
    return df


def clean_data(df):
    """
    Basic cleaning
    """

    # Remove customerID
    if "customerID" in df.columns:
        df.drop("customerID", axis=1, inplace=True)

    # Convert TotalCharges to numeric
    df["TotalCharges"] = pd.to_numeric(
        df["TotalCharges"],
        errors="coerce"
    )

    # Fill missing values
    df["TotalCharges"] = df["TotalCharges"].fillna(
        df["TotalCharges"].median()
    )
    


    return df


def encode_data(df):
    """
    Encode categorical columns
    """

    encoder = LabelEncoder()

    categorical_cols = df.select_dtypes(
        include=["object"]
    ).columns

    for col in categorical_cols:
        df[col] = encoder.fit_transform(df[col])

    return df


def split_data(df):

    X = df.drop("Churn", axis=1)

    y = df["Churn"]

    X_train, X_test, y_train, y_test = train_test_split(
        X,
        y,
        test_size=0.2,
        random_state=42,
        stratify=y
    )

    return X_train, X_test, y_train, y_test