#!/usr/bin/python3
"""
    A file that contains the definition of the class 'Finish'.
"""

from models.base_model import BaseModel, Base
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

class Finish(BaseModel, Base):
    """
        Define the class 'Finish' which inherits from 'BaseModel' and 'Base'.
    """
    __tablename__ = "finishes"
    tourney_id = Column(String(60), ForeignKey('tourneys.id'), nullable=False)
    team_id = Column(String(60), ForeignKey('teams.id'), nullable=False)
    placement = Column(Integer, default=0, nullable=False)

    tourneys = relationship('Tourney', cascade='delete', backref='finish')
    teams = relationship('Team', cascade='delete', backref='finish')
