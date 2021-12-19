from DataAccess.EngineConnector.EngineContext import *


class Guvernare(EngineContext.Base):
    __tablename__ = "Guvernare"
    id_tara = Column(Integer(), ForeignKey('Tara.id'), primary_key=True)
    sistem_politic = Column(String())
    presedinte = Column(String())
    vice_presedinte = Column(String())
    prim_ministru = Column(String())


if __name__ == "__main__":
    EngineContext.save()
