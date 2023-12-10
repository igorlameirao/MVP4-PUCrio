import pickle
from fastapi import FastAPI, APIRouter
from dtos.request import MachineReqModel
from sklearn.metrics import accuracy_score # para a exibição da acurácia do modelo
from Test.modelo import Model
import joblib
# from entities import Machine, Session

router = APIRouter(prefix='/machine', tags=["Machine"])


@router.post("")
def submit(model: MachineReqModel):

    path_modelo = "model/modelo.pkl"
    scaler_path = joblib.load("model/scaler.joblib")
    modelo = Model.carrega_modelo(path_modelo, scaler_path)
    predicao = Model.resultado_predicao(modelo, model),

    if predicao[0] == 1:
        return 'Boa qualidade'
    else:
        return 'Qualodade ruim'


def include_route(app: FastAPI):
    app.include_router(router)
