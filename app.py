from flask import  Flask, render_template, url_for, request, redirect
from datetime import datetime
from flask_sqlalchemy import  SQLAlchemy
import routing

app = Flask(__name__)

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False # 'это уже не поддерживается'
app.config['SEND_FILE_MAX_AGE_DEFAULT'] = False
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///sblog.db'# создание базы данных
db = SQLAlchemy(app)
#db.create_all() создание базы

class Article(db.Model):# класс обьектов, которые будем хранить в базе
     id = db.Column(db.Integer, primary_key = True)
     title = db.Column(db.String(100), nullable = False)
     intro = db.Column(db.String(300), nullable = False)
     TheText = db.Column(db.Text, nullable = False)
     date = db.Column(db.DateTime, default = datetime.utcnow)
     def __repr__(self):
         return '<Article %r' % self.id








if __name__ == "__main__":
    app.run(debug=True);
