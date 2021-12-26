from DataAccess.EngineConnector.EngineContext import *


class Guvernare(EngineContext.Base):
    __tablename__ = "Guvernare"

    id_tara = Column(Integer(), ForeignKey('Tara.id'), primary_key=True)
    sistem_politic = Column(String())
    presedinte = Column(String())
    link_presedinte = Column(String())
    prim_ministru = Column(String())
    link_prim_ministru = Column(String())
