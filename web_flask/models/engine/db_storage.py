#!/usr/bin/python3
"""
DBStorage class
"""

from os import getenv
from models.base_model import BaseModel, Base
from models.state import State
from models.city import City
from models.user import User
from models.place import Place
from models.review import Review
from models.amenity import Amenity
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker

class DBStorage:
    """
    DBStorage class
    """
    
    __engine = None
    __session = None

    def __init__(self):
        """
        Constructor method
        """
        self.__engine = create_engine('mysql+mysqldb://{}:{}@{}/{}'
                                      .format(getenv('HBNB_MYSQL_USER'),
                                              getenv('HBNB_MYSQL_PWD'),
                                              getenv('HBNB_MYSQL_HOST'),
                                              getenv('HBNB_MYSQL_DB')),
                                      pool_pre_ping=True)

        if getenv('HBNB_ENV') == 'test':
            Base.metadata.drop_all(bind=self.__engine)

    def all(self, cls=None):
        """
        Query on the current database session (self.__session) all objects
        depending of the class name (argument cls)
        """
        result = {}
        classes = [State, City, User, Place, Review, Amenity]
        if cls:
            objects = self.__session.query(cls).all()
        else:
            objects = []
            for c in classes:
                objects += self.__session.query(c).all()

        for obj in objects:
            key = obj.__class__.__name__ + '.' + obj.id
            result[key] = obj
        return result

    def new(self, obj):
        """
        Add the object to the current database session (self.__session)
        """
        self.__session.add(obj)

    def save(self):
        """
        Commit all changes of the current database session (self.__session)
        """
        self.__session.commit()

    def delete(self, obj=None):
        """
        Delete from the current database session obj if not None
        """
        if obj:
            self.__session.delete(obj)

    def reload(self):
        """
        Create all tables in the database (feature of SQLAlchemy)
        """
        Base.metadata.create_all(self.__engine)
        session_factory = sessionmaker(bind=self.__engine,
                                       expire_on_commit=False)
        Session = scoped_session(session_factory)
        self.__session = Session()

    def close(self):
        """
        Calls remove method on the private session attribute (self.__session)
        or close() on the class Session
        """
        self.__session.close()

