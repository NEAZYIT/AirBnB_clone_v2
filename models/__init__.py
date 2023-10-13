#!/usr/bin/python3
""" Initialize the BaseModel class with provided attributes or
default values.
"""
from models.engine.file_storage import FileStorage
from models.base_model import BaseModel

storage = FileStorage()
storage.reload()
BaseModel().register()
