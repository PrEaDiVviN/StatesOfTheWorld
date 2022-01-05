from DataAccess.EngineConnector.EngineContext import *


class Tara_Steaguri(EngineContext.Base):
    """A class used to represent a TaraSteaguri entity from Database. Used by 'sqlalchemy' orm to be able to work with the database."""
    __tablename__ = "Tara_Steaguri"

    id_tara = Column(Integer(), ForeignKey('Tara.id'), primary_key=True)
    drapel_link = Column(String())
    stema_link = Column(String())
