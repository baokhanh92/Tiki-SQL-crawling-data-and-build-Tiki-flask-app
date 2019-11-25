
from flask import Flask, request, jsonify, render_template
from flask_sqlalchemy import SQLAlchemy
import os 

app = Flask(__name__)

app.config.from_object('config.DevelopmentConfig')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

from models import Products
from models import Category

@app.route("/home")
def get_prod_by_cate():
    try:
        cate = Category.query().filter_by(name=name_)
        categories = [dict(e.serialize()) for e in cate]
        return render_template('home.html', articles=categories)

    except Exception as err:
        return(str(err))

@app.route("/product/getseller/<seller_>")
def get_prod_by_seller(seller_):
    try:
        product = Products.query.filter_by(seller=seller_)
        products = [dict(e.serialize()) for e in product]
        return render_template('index.html', articles=products)

    except Exception as err:
        return(str(err))

@app.route("/details")
def get_book_details():
    author=request.args.get('author')
    published=request.args.get('published')
    return "Author : {}, Published: {}".format(author,published)

if __name__ == '__main__':
    app.run()
