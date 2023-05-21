"""Seed file to make sample data for blogly db"""

from models import db, User
from app import app

# Create all tables
db.drop_all()
db.create_all()

# If table isn't empty, empty it
User.query.delete()

# Add users
Alan = User(first_name='Alan', last_name='Alda', image_url='https://i0.web.de/image/938/34260938,pd=1/alan-walker.jpg')
Joel = User(first_name='Joel', last_name='Burton', image_url='https://wtop.com/wp-content/uploads/2017/01/joel-mchale2.jpg')
Jane = User(first_name='Jane', last_name='Smith', image_url='https://i.pinimg.com/originals/37/e4/82/37e4825fb2e5d4f775746752e0ae79d2.jpg')

# Add new objects to session
db.session.add(Alan)
db.session.add(Joel)
db.session.add(Jane)

# Commit
db.session.commit()
