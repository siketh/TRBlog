#!flask/bin/python

from app import models, engine

print("Creating database schemas...")

models.Base.metadata.create_all(engine)