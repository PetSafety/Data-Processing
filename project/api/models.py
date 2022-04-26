from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.dialects import postgresql
import uuid

db = SQLAlchemy()


class DadosEmbarcado(db.Model):
    __tablename__ = "dados_embarcado"

    iddado = db.Column(db.Integer, primary_key=True, autoincrement=True)
    temperatura = db.Column(db.Text, nullable=False)
    ruido = db.Column(db.Text, nullable=False)
    video = db.Column(db.Text, nullable=False)
    idCaixa = db.Column(db.Integer, nullable=False)

    def __init__(
            self,
            temperatura,
            ruido,
            video,
            idCaixa
            
    ):
        self.temperatura = temperatura
        self.ruido = ruido
        self.video = video
        self.idCaixa = idCaixa

    def to_json(self):
        return {
            "iddado": self.iddado,
            "temperatura": self.temperatura,
            "ruido": self.ruido,
            "video": self.video,
            "idCaixa": self.idCaixa
        }
