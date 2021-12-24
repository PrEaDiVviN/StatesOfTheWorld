from sqlalchemy.orm import sessionmaker
from sqlalchemy.sql.expression import func
from DataAccess.Models import Tara, Economie, Geografie, GeografieVecini, Guvernare, Identificator, Limba, Populatie, TaraSteaguri
from DataAccess.EngineConnector.EngineContext import EngineContext


class PersistenceService:
    def __init__(self):
        self.Tara = Tara.Tara
        self.Economie = Economie.Economie
        self.Geografie = Geografie.Geografie
        self.GeografieVecini = GeografieVecini.Geografie_Vecini
        self.Guvernare = Guvernare.Guvernare
        self.Identificator = Identificator.Identificatori
        self.Limba = Limba.Limba
        self.Populatie = Populatie.Populatie
        self.TaraSteaguri = TaraSteaguri.Tara_Steaguri
        self.Engine = EngineContext()
        self.Session = sessionmaker()
        self.Session.configure(bind=self.Engine.engine)
        self.persisence_session = self.Session()
        self.func = func

    def add_item(self, item):
        self.persisence_session.add(item)

    def save(self):
        self.persisence_session.commit()
        self.persisence_session.close()

