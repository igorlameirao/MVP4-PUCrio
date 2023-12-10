import numpy as np
import pickle
import joblib


class Model:
    def carrega_modelo(path, scaler_path=None):

        if path.endswith(".pkl"):
            model = pickle.load(open(path, "rb"))
        elif path.endswith(".joblib"):
            model = joblib.load(path)
        else:
            raise Exception("Formato de arquivo invalido")

        if scaler_path is not None:
            model.scaler = scaler_path

        return model

    def resultado_predicao(model, form):
        X_input = np.array(
            [
                form.acidezFixa,
                form.acidezVolatil,
                form.acidoCitrico,
                form.acucarResidual,
                form.cloretos,
                form.dioxidoEnxofreLivre,
                form.dioxidoEnxofreTotal,
                form.densidade,
                form.ph,
                form.sulfatos,
                form.alcool
            ]
        )

        X_input = X_input.reshape(1, -1)
        X_input_scaled = model.scaler.transform(X_input)
        diagnostico = model.predict(X_input_scaled.reshape(1, -1))

        return int(diagnostico[0])
