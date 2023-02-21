""" Movies Model """
from models import database

class Movies(database.Model):
    """ Class for the movies table """
    id = database.Column(database.Integer, primary_key=True)
    title = database.Column(database.String(80), nullable=False)
    description = database.Column(database.String(120), nullable=False)
    release_year = database.Column(database.Integer, nullable=False)
    
    def to_dict(self) -> dict:
        """ Method to convert the object to a dictionary """
        return {
            "id": self.id,
            "title": self.title,
            "description": self.description,
            "release_year": self.release_yer
        }
    
    def __repr__(self) -> str:
        return f"Movie: {self.title}"