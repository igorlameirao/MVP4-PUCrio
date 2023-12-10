from pydantic import BaseModel

class MachineReqModel(BaseModel):
    acidezFixa: float
    acidezVolatil: float
    acidoCitrico: float
    acucarResidual: float
    cloretos: float
    dioxidoEnxofreLivre: float
    dioxidoEnxofreTotal: float
    densidade: float
    ph: float
    sulfatos: float
    alcool: float
