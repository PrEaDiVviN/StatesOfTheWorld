from DataAccess.EngineConnector.EngineContext import *


class Limba(EngineContext.Base):
    __tablename__ = "Limba"

    id_tara = Column(Integer(), ForeignKey('Tara.id'), primary_key=True)
    limba_oficiala = Column(String())
    link_limba_oficiala = Column(String())
    etnonime = Column(String())
    limbi_regionale_minoritate = Column(String())
