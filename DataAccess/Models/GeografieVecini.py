from DataAccess.EngineConnector.EngineContext import *


class Geografie_Vecini(EngineContext.Base):
    __tablename__ = "Geografie_Vecini"
    id_tara = Column(Integer(), ForeignKey('Tara.id'), primary_key=True)
    nume_vecin = Column(String())
