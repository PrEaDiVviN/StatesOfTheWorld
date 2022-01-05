from sqlalchemy import Column, Integer, String
from sqlalchemy import ForeignKey
from DataAccess.EngineConnector.config import Config
from sqlalchemy.orm import declarative_base
from sqlalchemy import create_engine


class EngineContext:
    """ A wrapper over sqlalchemy engine which loads the data about database from "./config.py". Mainly used
    to creates the entities in the database.
    """
    database_url = Config.database_connector + '://' + Config.username + ':' + Config.password + '@' + Config.host + ':' \
                   + Config.port + '/' + Config.database_name
    engine = create_engine(database_url, echo=False)
    Base = declarative_base()

    @staticmethod
    def save():
        """ A static functions that uses the current environment entities and creates them to the databases if they
        not exist.
        """
        EngineContext.Base.metadata.create_all(EngineContext.engine)
