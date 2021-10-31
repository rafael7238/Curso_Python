#pip install flask
#pip install flask_sqlalchemy
#pip install mysql-connector-python
#pip install mysqlclient

from flask import Flask,Response,Request
from flask_sqlalchemy import SQLAlchemy
import mysql.connector
import json

app=Flask(__name__)
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"]=True
                                      #mysql://username:password@server/db
app.config["SQLALCHEMY_DATABASE_URI"]="mysql://root:rafael19@localhost/teste"

db = SQLAlchemy(app)

class Usuario(db.Model):
    id = db.Column(db.Integer,primary_key=True)
    nome = db.Column(db.String(50))
    email = db.Column(db.String(100))

#db.create_all()

#Selecionar Tudo
#Selecionar Um
#Selec