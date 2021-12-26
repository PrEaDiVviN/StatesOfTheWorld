from sqlalchemy import Column, Integer, String
from sqlalchemy import ForeignKey
from DataAccess.EngineConnector.config import Config
from sqlalchemy.orm import declarative_base
from sqlalchemy import create_engine


class EngineContext:
    database_url = Config.database_connector + '://' + Config.username + ':' + Config.password + '@' + Config.host + ':' \
                   + Config.port + '/' + Config.database_name
    engine = create_engine(database_url, echo=True)
    Base = declarative_base()

    @staticmethod
    def save():
        EngineContext.Base.metadata.create_all(EngineContext.engine)
