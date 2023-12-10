import pandas as pd

from avaliador import Avaliador
from modelo import Model

modelo = Model()
avaliador = Avaliador()

# Parâmetros
url_dados = "https://raw.githubusercontent.com/igorlameirao/MVP4-PUCrio/main/Vinho-DataSet.csv"
colunas = [
    "acidezFixa",
    "acidezVolatil",
    "acidoCitrico",
    "acucarResidual",
    "cloretos",
    "dioxidoEnxofreLivre",
    "dioxidoEnxofreTotal",
    "densidade",
    "ph",
    "sulfatos",
    "alcool",
    "qualidade"
]

# Carga dos dados
dataset = pd.read_csv(url_dados, names=colunas, skiprows=1, delimiter=",")

# Remove as linhas com valores NaN
dataset = dataset.dropna()

X = dataset.iloc[:,0:11]
Y = dataset.iloc[:,11]

Y = Y.astype(int)

print("Valores de entrada X:")
print(X)

print("\nValores de saída Y:")
print(Y)

def test_modelo_lr():
    modelo_lr = Model.carrega_modelo("../model/modelo_lr.pkl")

    acuracia_lr, recall_lr, precisao_lr, f1_lr = avaliador.avaliar(modelo_lr, X, Y)

    assert acuracia_lr >= 0.6
    assert recall_lr >= 0.5
    assert precisao_lr >= 0.5
    assert f1_lr >= 0.5

def test_modelo_knn():
    modelo = Model.carrega_modelo("../model/modelo.pkl")

    acuracia_knn, recall_knn, precisao_knn, f1_knn = avaliador.avaliar(modelo, X, Y)

    assert acuracia_knn >= 0.4
    assert recall_knn >= 0.1
    assert precisao_knn >= 0.5
    assert f1_knn >= 0.2

def test_modelo():
    modelo = Model.carrega_modelo("../model/modelo.pkl")

    acuracia, recall, precisao, f1 = avaliador.avaliar(modelo, X, Y)

    assert acuracia >= 0.4
    assert recall >= 0.1
    assert precisao >= 0.5
    assert f1 >= 0.2
