from DataAccess.EngineConnector.EngineContext import *


class Guvernare(EngineContext.Base):
    """A class used to represent a Guvernare entity from Database. Used by 'sqlalchemy' orm to be able to work with the database."""
    __tablename__ = "Guvernare"

    id_tara = Column(Integer(), ForeignKey('Tara.id'), primary_key=True)
    sistem_politic = Column(String())
    presedinte = Column(String())
    link_presedinte = Column(String())
    prim_ministru = Column(String())
    link_prim_ministru = Column(String())
