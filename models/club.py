#!/usr/bin/python3
"""
    A file that contains the definition of the class 'Club'.
"""

from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, ForeignKey
# from sqlalchemy.org import relationship

class Club(BaseModel, Base):
    """
        Define the class 'Club' which inherits from 'BaseModel' and 'Base'.
    """
    __tablename__ = "clubs"
    # name_long = Column(String(128), nullable=False)
    name_short = Column(String(64), nullable=False)
    # pool_primary = Column(String(256), nullable=False)
        # Murrieta Valley High School, MVHS Pool,
        # 41220 Nighthawk Way, Murrieta, California, USA, 92562
    # tuition_min = Column(Integer, default=0, nullable=False)
    # tuition_max = Column(Integer, default=0, nullable=False)
