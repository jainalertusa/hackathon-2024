from flask_sqlalchemy import SQLAlchemy
import csv

db = SQLAlchemy()

class ScrapedData(db.Model):
    __tablename__ = 'scraped_data'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    first_line = db.Column(db.String(255))
    city = db.Column(db.String(100))
    state = db.Column(db.String(50))
    zip_code = db.Column(db.String(20))
    full_address = db.Column(db.String(255), unique=True)
    price = db.Column(db.String(50))
    seller = db.Column(db.String(255))
    beds = db.Column(db.String(10))
    baths = db.Column(db.String(10))
    sqft = db.Column(db.String(100))  # Adjusted size for sqft
    score = db.Column(db.Float)
    ppsf = db.Column(db.Float)  # New column for Price Per Square Foot

class MedianPPSF(db.Model):
    __tablename__ = 'median_ppsf'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    city = db.Column(db.String(100))
    state = db.Column(db.String(50))
    m_ppsf = db.Column(db.Float)

def create_tables():
    db.create_all()