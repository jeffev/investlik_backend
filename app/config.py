from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

# Configuração do banco de dados PostgreSQL
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:123@localhost/investlink'

# Inicialização do Flask-SQLAlchemy
db = SQLAlchemy(app)
