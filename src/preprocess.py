from sklearn.preprocessing import LabelEncoder
import pandas as pd

def preprocess_data(df: pd.DataFrame) -> tuple:
    df = df.dropna()

    le = LabelEncoder()
    df['gender'] = le.fit_transform(df['gender'])
    df['churn'] = le.fit_transform(df['churn'])

    X = df.drop('churn', axis=1)
    y = df['churn']

    return X, y