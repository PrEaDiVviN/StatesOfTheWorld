from DataAccess.EngineConnector.EngineContext import *


class Geografie_Vecini(EngineContext.Base):
    """A class used to represent a Geografie_Vecini entity from Database. Used by 'sqlalchemy' orm to be able to work with the database."""
    __tablename__ = "Geografie_Vecini"

    id_tara = Column(Integer(), ForeignKey('Tara.id'), primary_key=True)
    nume_vecin = Column(String(), primary_key=True)
