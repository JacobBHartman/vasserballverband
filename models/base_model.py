#!/usr/bin/python3
"""
    This Python file contains a class called 'BaseModel' that defines all common
    attributes and methods for others classes.
"""
import os
import uuid
from datetime import datetime
import models
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, String, DateTime


Base = declarative_base()


class BaseModel:
    """
        Base class that unites common attributes across all classes of objects.
    """

    id = Column(String(60), nullable=False, primary_key=True)
    created_at = Column(DateTime, default=datetime.utcnow(), nullable=False)
    updated_at = Column(DateTime, default=datetime.utcnow(), nullable=False)

    def __init__(self, *args, **kwargs):
        """
            Initialize public instance attributes.
        """
        if (len(kwargs) == 0):
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
        else:
            try
                time_format = "%Y-%m-%dT%H:%M:%S.%f"
                kwargs["created_at"] = datetime.strptime(kwargs["created_at"],
                                                         time_format)
                kwargs["updated_at"] = datetime.strptime(kwargs["updated_at"],
                                                         time_format)
            except KeyError:
                self.id = str(uuid.uuid4())
                self.created_at = datetime.now()
                self.updated_at = datetime.now()
            for key, val in kwargs.items():
                if "__class__" not in key:
                    setattr(self, key, val)

    def __str__(self):
        """
            Return the string representation of a 'BaseModel' class instance.
        """
        return ("[{}] ({}) {}".format(self.__class__.__name__,
                                      self.id, self.__dict__))

    def __repr__(self):
        """
            Return the string representation of a 'BaseModel' class instance.
        """
        return ("[{}] ({}) {}".format(self.__class__.__name__,
                                      self.id, self.__dict__))

    def save(self):
        """
            Update the 'updated_at' attribute.
        """
        self.updated_at = datetime.now()
        models.storage.new(self)
        models.storage.save()

    def to_dict(self):
        """
            Return the dictionary representation of a 'BaseModel' class
            instance.
        """
        ret_dict = dict(self.__dict__)
        try:
            del ret_dict['_sa_instance_state']
        except KeyError:
            pass
        ret_dict['__class__'] = self.__class__.__name__
        ret_dict['updated_at'] = self.updated_at.strftime("%Y-%m-%dT%H:%M:%S.%f")
        ret_dict['created_at'] = self.created_at.strftime("%Y-%m-%dT%H:%M:%S.%f")

        return ret_dict

    def delete(self):
        """
            Delete the current instance from storage.
        """
        models.storage.delete(self)
