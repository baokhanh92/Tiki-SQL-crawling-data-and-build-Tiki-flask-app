from flask_sqlalchemy import SQLAlchemy
import os
from flask import Flask, request, jsonify
import psycopg2

app = Flask(__name__)
db = SQLAlchemy(app)

class Products(db.Model):
    __tablename__ = 'products'

    id = db.Column(db.Integer, primary_key=True)
    images = db.Column(db.String())
    fprice = db.Column(db.String())
    category = db.Column(db.String())
    subcategory = db.Column(db.String())
    titles = db.Column(db.String())
    seller = db.Column(db.String())
    rprice = db.Column(db.String())
    discount = db.Column(db.String())
    ratings = db.Column(db.String())
    num_reviews = db.Column(db.String())
    tikinow = db.Column(db.String())
    productlink = db.Column(db.String())

    def __init__(self, id, images, fprice, category, subcategory, titles, seller, rprice, discount, ratings, num_reviews, tikinow, productlink ):
        self.id = id
        self.images = images
        self.fprice = fprice
        self.category = category
        self.subcategory = subcategory
        self.titles = titles
        self.seller = seller
        self.rprice = rprice
        self.discount = discount
        self.ratings = ratings
        self.num_reviews = num_reviews
        self.tikinow = tikinow
        self.productlink = productlink

    def __repr__(self):
        return '<id {}>'.format(self.id)
    
    def serialize(self):
        return {
            'id' : self.id,
            'images' : self.images,
            'fprice' : self.fprice,
            'category' : self.category,
            'subcategory' : self.subcategory,
            'titles' : self.titles,
            'seller' : self.seller,
            'rprice' : self.rprice,
            'discount' : self.discount,
            'ratings' : self.ratings,
            'num_reviews' : self.num_reviews,
            'tikinow' : self.tikinow,
            'productlink' : self.productlink
        }

class Category(db.Model):
    __tablename__ = 'categories'
    cat_id = db.Column(db.Integer(), primary_key=True)
    name = db.Column(db.String())
    url = db.Column(db.String())
    parent_id = db.Column(db.Integer())

    def __init__(self, cat_id, name, url, parent_id):
        self.cat_id = cat_id
        self.name = name
        self.url = url
        self.parent_id = parent_id
        
        
    def __repr__(self):
        return f'ID: {self.cat_id}, Name: {self.name}, URL: {self.url}, Parent ID: {self.parent_id}'

    def serialize(self):
        return {
            'cat_id' : self.cat_id,
            'name' : self.name,
            'url' : self.url,
            'parent_id' : self.parent_id,
        }