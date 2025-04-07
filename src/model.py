import mlflow
import mlflow.sklearn
import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, classification_report
from sklearn.model_selection import train_test_split
import joblib

def load_and_preprocess_data():
    print("Carregando os dados...")
    data = pd.read_csv("dados/dados_clientes.csv")

    print("Pré-processando os dados...")
    X = data.drop("churn", axis=1)
    y = data["churn"]

    X = X.apply(lambda col: col.astype('float64') if col.dtype == 'int64' else col)

    return X, y

def train_and_evaluate(X, y):
    print("Treinando o modelo...")
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    model = RandomForestClassifier(n_estimators=100, random_state=42)
    model.fit(X_train, y_train)

    y_pred = model.predict(X_test)
    acc = accuracy_score(y_test, y_pred)

    print("Relatório de Classificação:")
    print(classification_report(y_test, y_pred))
    print("Acurácia:", acc)

    mlflow.log_param("n_estimators", 100)
    mlflow.log_param("random_state", 42)
    mlflow.log_metric("accuracy", acc)

    input_example = pd.DataFrame([X_test.iloc[0]])
    mlflow.sklearn.log_model(model, "model", input_example=input_example)

    joblib.dump(model, "modelo_churn.pkl")

    return model

def main():
    X, y = load_and_preprocess_data()
    train_and_evaluate(X, y)

if __name__ == "__main__":
    main()
