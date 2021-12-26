from DataAccess.EngineConnector.EngineContext import *


class Populatie(EngineContext.Base):
    __tablename__ = "Populatie"

    id_tara = Column(Integer(), ForeignKey('Tara.id'), primary_key=True)
    recensamant_populatie = Column(String())
    densitate_populatie = Column(String())
