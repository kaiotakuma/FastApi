from sqlalchemy.orm import Session
from src.schemas import schemas
from src.infra.sqlachemy.models import models

class RepositorioDerie():

    def _init_(self,db:Session):
        self.db = db

    def criar(self,serie:schemas.Serie):
        db_serie = models.Serie(titulo=serie.titulo,
                                ano = serie.ano,
                                genero = serie.genero,
                                qtdTemporadas = serie.qtdTemporadas)
        self.db.add(db_serie)
        self.db.commit()
        self.db.refresh(db_serie)
        return db_serie

    def listar(self):
        series = self.db.query(models.Serie),all()
    def obter(self):
        pass
    def remover(self):
        pass
