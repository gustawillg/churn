import mlflow
import mlflow.sklearn
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, classification_report
from sklearn.model_selection import train_test_split
import joblib

def train_and_evaluate(X, y):
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

    model_path = "modelo_churn.pkl"
    joblib.dump(model, model_path)  

    mlflow.sklearn.log_model(model, "model")

    return model
