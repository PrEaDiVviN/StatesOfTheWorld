from DataAccess.EngineConnector.EngineContext import *


class Geografie(EngineContext.Base):
    __tablename__ = "Geografie"

    id_tara = Column(Integer(), ForeignKey('Tara.id'), primary_key=True)
    suprafata_totala = Column(String())
    apa_procent_suprafata_totala = Column(String())
    cel_mai_inalt_punct_nume = Column(String())
    link_cel_mai_inalt_punct = Column(String())
    cel_mai_inalt_punct_inaltime = Column(String())
    cel_mai_jos_punct_nume = Column(String())
    link_cel_mai_jos_punct = Column(String())
    cel_mai_jos_punct_inaltime = Column(String())
    fus_orar = Column(String())
