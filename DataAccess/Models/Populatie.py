from DataAccess.EngineConnector.EngineContext import *


class Populatie(EngineContext.Base):
    __tablename__ = "Populatie"
    id_tara = Column(Integer(), ForeignKey('Tara.id'), primary_key=True)
    recensamant_specificatie = Column(String())
    recensamant_populatie = Column(Integer())
    densitate_populatie = Column(Integer())
