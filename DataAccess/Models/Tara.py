from DataAccess.EngineConnector.EngineContext import *


class Tara(EngineContext.Base):
    """A class used to represent a Tara entity from Database. Used by 'sqlalchemy' orm to be able to work with the database."""
    __tablename__ = 'Tara'

    id = Column(Integer(), primary_key=True)
    nume_scurt = Column(String())
    nume_oficial = Column(String())
    capitala = Column(String())
    link_tara = Column(String())
    link_capitala = Column(String())
