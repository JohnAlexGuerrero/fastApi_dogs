from peewee import Model
from peewee import CharField
from db.databases import databases

class BaseModel(Model):
    class Meta:
        database = databases

class User(BaseModel):
    email = CharField(max_length=50, unique=True)
    hashed_password = CharField(max_length=100)
    

    
