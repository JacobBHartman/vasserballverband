#!/usr/bin/python3
"""
    A file that contains the definition of the class 'Team'.
"""

from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, ForeignKey
# from sqlalchemy.org import relationship

class Team(BaseModel, Base):
    """
        Define the class 'Team' which inherits from 'BaseModel' and 'Base'.
    """
    __tablename__ = 'teams'
    group = Column(String(4), default='', nullable=False)
    club_id = Column(String(60), ForeignKey('clubs.id'), nullable=False)
