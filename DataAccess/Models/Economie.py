from DataAccess.EngineConnector.EngineContext import *


class Economie(EngineContext.Base):
    """A class used to represent an Economie entity from Database. Used by 'sqlalchemy' orm to be able to work with the database."""
    __tablename__ = "Economie"

    id_tara = Column(Integer(), ForeignKey('Tara.id'), primary_key=True)
    pib_ppc_total = Column(String())
    pib_ppc_cap_locuitor = Column(String())
    pib_nominal_total = Column(String())
    pib_nominal_cap_locuitor = Column(String())
    gini = Column(String())
    idu = Column(String())
    moneda = Column(String())
