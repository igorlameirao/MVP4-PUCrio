from sqlalchemy import Column, String, Integer
from entities import Base

class Machine(Base):
    __tablename__ = 'Machine'

    id = Column(Integer, primary_key=True)
    nome = Column(String(140))
    sobrenome = Column(String(140))
    cep = Column(String(140))
    logradouro = Column(String(140))
    complemento = Column(String(140))
    bairro = Column(String(140))

    def __init__(self, nome: str, sobrenome: str, cep: str, logradouro: str, complemento: str, bairro: str ):
        self.nome = nome
        self.sobrenome = sobrenome
        self.cep = cep
        self.logradouro = logradouro
        self.complemento = complemento
        self.bairro = bairro
