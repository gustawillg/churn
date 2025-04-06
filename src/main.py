from data_loader import load_data
from preprocess import preprocess_data
from model import train_and_evaluate

def main():
    print("Carregando os dados...")
    df = load_data("data/churn.csv")

    print("Pré-processando os dados...")
    X, y = preprocess_data(df)

    print("Treinando o modelo...")
    train_and_evaluate(X, y)

if __name__ == "__main__":
    main()