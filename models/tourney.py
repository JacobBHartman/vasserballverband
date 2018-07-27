#!/usr/bin/python3
"""
    A file that contains the definition of the class 'Tourney'.
"""

from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, ForeignKey

class Tourney(BaseModel, Base):
    """
        Define the class 'Tourney' which inherits from 'BaseModel' and 'Base'.
    """
    __tablename__ = 'tourneys'
    name = Column(String(60), default='', nullable=False)
    group = Column(String(4), default='', nullalbe=False)
    size = Column(Integer, default=1, nullable=False)
    finishes = relationship('Finish', backref='tourney', cascade='delete')
