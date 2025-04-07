from sklearn.preprocessing import LabelEncoder
import pandas as pd

def preprocess_data(df: pd.DataFrame) -> tuple:
    df.columns = df.columns.str.strip()
    df = df.dropna()  

    if 'customerID' in df.columns:
        df = df.drop('customerID', axis=1)

    le = LabelEncoder()
    for col in df.select_dtypes(include='object').columns:
        df[col] = le.fit_transform(df[col])

    X = df.drop('Churn', axis=1)
    y = df['Churn']

    return X, y
