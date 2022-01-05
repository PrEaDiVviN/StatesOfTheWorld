from DataAccess.EngineConnector.EngineContext import *


class Limba(EngineContext.Base):
    """A class used to represent a Limba entity from Database. Used by 'sqlalchemy' orm to be able to work with the database."""
    __tablename__ = "Limba"

    id_tara = Column(Integer(), ForeignKey('Tara.id'), primary_key=True)
    limba_oficiala = Column(String())
    link_limba_oficiala = Column(String())
    etnonime = Column(String())
    limbi_regionale_minoritate = Column(String())
