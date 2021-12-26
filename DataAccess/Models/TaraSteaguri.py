from DataAccess.EngineConnector.EngineContext import *


class Tara_Steaguri(EngineContext.Base):
    __tablename__ = "Tara_Steaguri"

    id_tara = Column(Integer(), ForeignKey('Tara.id'), primary_key=True)
    drapel_link = Column(String())
    stema_link = Column(String())
