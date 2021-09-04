from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

from products import products

@app.route('/ping')
def ping():
  return jsonify({ "message": "pong!" })

@app.route('/products')
def getProducts():
  return jsonify({'products': products})

