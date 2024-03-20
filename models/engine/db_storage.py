#!/usr/bin/python3
""" DBStorage """
from os import getenv
from sqlalchemy.orm import sessionmaker, scoped_session
from sqlalchemy import create_engine
from models.base_model import BaseModel, Base
from models.state import State
from models.city import City
from models.user import User
from models.place import Place
from models.review import Review
from models.amenity import Amenity


class DBStorage():
    """class DBStorage"""
    __engine = None
    __session = None

    classes = {
            "User": User,
            "State": State,
            "City": City,
            "Amenity": Amenity,
            "Place": Place,
            "Review": Review}

    def __init__(self):
        """Initialization method"""
        user = getenv("HBNB_MYSQL_USER")
        password = getenv("HBNB_MYSQL_PWD")
        host = getenv("HBNB_MYSQL_HOST", default="localhost")
        db = getenv("HBNB_MYSQL_DB")

        DBStorage.__engine = create_engine(
                f'mysql+mysqldb://{user}:{password}@{host}/{db}', pool_pre_ping=True)

        if getenv("HBNB_ENV") == "test":
            Base.metadata.drop_all(DBStorage.__engine)

    def all(self, cls=None):
        """query tables"""
        result_dict = {}
        if cls:
            list_obj = DBStorage.__session.query(cls).all()
            for obj in list_obj:
                key = obj.to_dict()['__class__'] + '.' + obj.id
                result_dict[key] = obj
        else:
            list_obj = []
            for model_cls in DBStorage.classes.values():
                try:
                    list_obj.extend(DBStorage.__session.query(model_cls).all())
                except:
                    pass
            for obj in list_obj:
                key = obj.to_dict()['__class__'] + '.' + obj.id
                result_dict[key] = obj

        return result_dict

    def new(self, obj):
        """new object"""
        DBStorage.__session.add(obj)

    def save(self):
        """saves objects"""
        DBStorage.__session.commit()

    def delete(self, obj=None):
        """delete object"""
        if obj:
            DBStorage.__session.delete(obj)
            DBStorage.__session.commit()

    def reload(self):
        """Create tables"""
        Base.metadata.create_all(self.__engine)
        Session = sessionmaker(bind=self.__engine, expire_on_commit=False)
        DBStorage.__session = scoped_session(Sesssion)

    def close(self):
        """remove session"""
        DBStorage.__session.close()
