from DataAccess.EngineConnector.EngineContext import *


class Populatie(EngineContext.Base):
    """A class used to represent a Populatie entity from Database. Used by 'sqlalchemy' orm to be able to work with the database."""
    __tablename__ = "Populatie"

    id_tara = Column(Integer(), ForeignKey('Tara.id'), primary_key=True)
    recensamant_populatie = Column(String())
    densitate_populatie = Column(String())
