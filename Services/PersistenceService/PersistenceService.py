from sqlalchemy.orm import sessionmaker
from sqlalchemy.sql.expression import func
from DataAccess.Models import Tara, Economie, Geografie, GeografieVecini, Guvernare, Identificator, Limba, Populatie, TaraSteaguri
from DataAccess.EngineConnector.EngineContext import EngineContext


class PersistenceService:
    """ A wrapping for sqlalchemy orm used to add entities to database. """
    def __init__(self):
        """Initialize PersistenceService with all existing entities in the database, a session to work on and a func
        sqlalchemy function.
        """
        self.Tara = Tara.Tara
        self.Economie = Economie.Economie
        self.Geografie = Geografie.Geografie
        self.GeografieVecini = GeografieVecini.Geografie_Vecini
        self.Guvernare = Guvernare.Guvernare
        self.Identificator = Identificator.Identificatori
        self.Limba = Limba.Limba
        self.Populatie = Populatie.Populatie
        self.TaraSteaguri = TaraSteaguri.Tara_Steaguri
        self.Engine = EngineContext()
        self.Session = sessionmaker()
        self.Session.configure(bind=self.Engine.engine)
        self.persisence_session = self.Session()
        self.func = func

    def add_item(self, item):
        """ A function that adds the current item to the current session.
        :param item: Database Entity (elements of this class)
        """
        self.persisence_session.add(item)

    def save(self):
        """ A function that saves the all the items in the current session to the database and closes the session. """
        self.persisence_session.commit()
        self.persisence_session.close()

