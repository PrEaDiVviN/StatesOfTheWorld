from DataAccess.EngineConnector.EngineContext import *


class Identificatori(EngineContext.Base):
    """A class used to represent an Identificatori entity from Database. Used by 'sqlalchemy' orm to be able to work with the database."""
    __tablename__ = "Identificatori"

    id_tara = Column(Integer(), ForeignKey('Tara.id'), primary_key=True)
    cod_cio = Column(String())
    cod_mobil = Column(String())
    prefix_mobil = Column(String())
    domeniu_internet = Column(String())
