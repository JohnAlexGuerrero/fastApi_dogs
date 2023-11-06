from peewee import CharField, ForeignKeyField
from peewee import Model
from db.databases import databases

class BaseModel(Model):
    class Meta():
        database = databases

class Bread(BaseModel):
    name = CharField(max_length=20, unique=True)
    
class Dog(BaseModel):
    name = CharField(max_length=100, unique=True)
    breed = ForeignKeyField(Bread, backref='dogs')