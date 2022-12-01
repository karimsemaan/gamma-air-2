from flask import Blueprint
import json
from src import db

pilots = Blueprint('pilots', __name__)

@pilots.route('/home', methods=['GET'])
def home():
    return '<h1>Pilots: Home</h1>'

