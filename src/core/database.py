from dotenv import dotenv_values
import random
from sqlalchemy import Column, BigInteger, MetaData, create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import scoped_session, sessionmaker, Session

config = dotenv_values(".env")

engines = {
    "primary": create_engine("postgresql://{}:{}@{}:{}/{}".format(
        config["DATABASE_PRIMARY_USER"],
        config["DATABASE_PRIMARY_PASSWORD"],
        config["DATABASE_PRIMARY_HOST"],
        config["DATABASE_PRIMARY_PORT"],
        config["DATABASE_PRIMARY_NAME"],
    ), logging_name="primary", echo=True),
    "secondary": create_engine("postgresql://{}:{}@{}:{}/{}".format(
        config["DATABASE_READ_USER"],
        config["DATABASE_READ_PASSWORD"],
        config["DATABASE_READ_HOST"],
        config["DATABASE_READ_PORT"],
        config["DATABASE_READ_NAME"],
    ), logging_name="secondary", echo=True)
}


class RoutingSession(Session):

    def get_bind(self, mapper=None, clause=None):
        if self._name:
            return engines[self._name]
        elif self._flushing:
            return engines["primary"]
        else:
            return engines[
                random.choice(["primary", "secondary"])
            ]

    _name = None

    def using_bind(self, name):
        s = RoutingSession()
        vars(s).update(vars(self))
        s._name = name
        return s


class Base(object):
    id = Column(BigInteger, primary_key=True)

    def __repr__(self):
        return "%s(id=%r)" % (
            self.__class__.__name__,
            self.id
        )


Base = declarative_base(cls=Base)

SessionLocal = scoped_session(sessionmaker(autocommit=True, class_=RoutingSession))
