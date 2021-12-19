from DataAccess.EngineConnector.EngineContext import *


class Identificatori(EngineContext.Base):
    __tablename__ = "Identificatori"
    id_tara = Column(Integer(), ForeignKey('Tara.id'), primary_key=True)
    cod_cio = Column(String())
    cod_mobil = Column(String())
    prefix_mobil = Column(String())
    domeniu_internet = Column(String())
