from flask import Flask
from flask_sqlalchemy import SQLAlchemy

# создание экземпляра приложения
app = Flask(__name__)

# инициализирует расширения
db = SQLAlchemy(app)

# import views
from . import views