from apps import app, db
from flask import render_template, request, redirect, url_for, flash, make_response, session
from datetime import datetime
from flask_sqlalchemy import SQLAlchemy
@app.route('/')
def index():
    return render_template('base_file.html')

@app.route('/create_article')
def create_article():
    return render_template('create_article.html')

@app.route('/index')
def indexx():
    return render_template('index.html')

@app.route('/about')
def aboutpost():
    return render_template('about.html')

@app.route('/create_article', methods = ['POST', 'GET'])
def NextSite():
    if request.method == "POST":
        title = request.form['title']
        intro = request.form['intro']
        text = request.form['text']

        article_for_db_setting = Article(title = title, intro = intro, TheText = text)  #создаём обьёкт который будем сеттить в bd

        try: #попытка сеттить в базу
            db.session.add(article_for_db_setting) # добавление в базу
            db.session.commit(); # применение изменений
            return redirect("/posts/")# в случае успешного добавления, перенапрявлем на "/"

        except:
            return "При добавлении возникла ошибка"

        # делаем что-то при методе получения из формы
    else:
        return render_template("create_article.html")
        #return "SecondSite.html" + name + str(id);



@app.route('/posts/') # отображение инфы из бд
def veiwPosts():
    #article = Article.query.first()  #обращяемся именно к той табличке которая отдена под статьи (12 строка)
    #article = Article.query.first()  # first - первая строка в таблице
    #article = Article.query.all()  # все записи  в таблице
    print('123')
    articles = Article.query.order_by(Article.date).all()  # все записи в таблице, метод  order_by(Artcie.<поле модели) #вертает массив данных из бд
    return render_template("posts.html", articles=articles); # передача массива для дальнейшего отображения массива в шаблон

@app.route('/reg/')
def regist():
    return render_template('TheOriginalReg.html')

class Article(db.Model):# создание таблицы 
    #__tablename__ = "Articles"
     id = db.Column(db.Integer, primary_key = True) #колонки таблицы
     title = db.Column(db.String(100), nullable = False)
     intro = db.Column(db.String(300), nullable = False)
     TheText = db.Column(db.Text, nullable = False)
     date = db.Column(db.DateTime, default = datetime.utcnow)
     def __repr__(self):
         return '<Article %r' % self.id