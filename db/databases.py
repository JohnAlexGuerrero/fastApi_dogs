from peewee import MySQLDatabase
from db.variables import NAME_DATABASE, USERNAME, PASSWORD

databases = MySQLDatabase(NAME_DATABASE, user=USERNAME, password=PASSWORD)