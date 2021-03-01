from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_script import Manager, Command, Shell
import os

# создание экземпляра приложения

app = Flask(__name__)
app.debug = True
#app.config.from_object(os.environ.get('FLASK_ENV') or 'config.DevelopementConfig')

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False # 'это уже не поддерживается'
app.config['SEND_FILE_MAX_AGE_DEFAULT'] = False
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///sblog.db'# создание базы данных

db = SQLAlchemy(app)

import views
#from views import views
# from . import forum_views
# from . import admin_views