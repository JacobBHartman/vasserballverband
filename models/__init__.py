#!/usr/bin/python3
"""
    A package initializer for the 'models' package.

    Create an instance of DBStorage() a.k.a. database storage instantiation.
"""

from models.base_model import BaseModel
from models.club import Club
from models.finish import Finish
from models.team import Team
from models.tourney import Tourney

classes = {
    'BaseModel': BaseModel,
    'Club': Club,
    'Finish': Finish,
    'Team': Team,
    'Tourney': Tourney
}

from models.engine.db_storage import DBStorage
storage = DBStorage()
storage.reload()
