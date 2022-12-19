"""Models for Blogly."""
 
from flask_sqlalchemy import SQLAlchemy

dp = SQLAlchemy()

DEFAULT_IMAGE_URL = "https://cdn.pixabay.com/photo/2015/10/05/22/37/blank-profile-picture-973460_960_720.png"

class User(db.Model):
    """USER"""

    __tablename__= "users"
    id = db.Column(db.Integer, primary_key = True)
    first_name = db.Column(db.Text, nullable = False)
    last_name = db.Column(db.Text, nullable = False)
    image_url = db.Column(db.Text, nullable = False, default = DEFAULT_IMAGE_URL)

    @property
    def full_name(self):
        """Combines into Full Name of User"""

        return f"{self.first_name} {self.last_name}"

def connect_db(app):
        """Conect this database to app"""
        db.app = app
        db.init_app(app)