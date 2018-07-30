#!/usr/bin/python3
'''
This file is the initializer for the Models module. It imports all Models and
the storage engine and creates a 'global' dictionary of all models. Upon each
initialization the `storage.reload()` method gets called which will read the
contents from storage and populate `FileStorage.__objects` with the deserialized
version of all objects.
'''

from models.base_model import BaseModel
from models.club import Club
from models.finish import Finish
from models.team import Team
from models.tourney import Tourney
import os


'''
CNC = { Class Name (string) : Class Type }
'''

#if os.environ.get('RENTABIKE_TYPE_STORAGE') == 'db':
from models.engine import db_storage
classes = db_storage.DBStorage.classes
storage = db_storage.DBStorage()
#else:
 #   from models.engine import file_storage
  #  CNC = file_storage.FileStorage.CNC
   # storage = file_storage.FileStorage()

storage.reload()
