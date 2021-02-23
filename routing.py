from app import app, Article

from flask import  Flask, render_template, url_for, request, redirect
from datetime import datetime
from flask_sqlalchemy import  SQLAlchemy

# роутинг двух ссылок видёт на отображение одной стронички
@app.route('/home')
@app.route('/')
def index():
    return render_template("index.html");


#роутинг стронички about
#@app.route('/<string:name>/<int:id>')
@app.route('/create', methods = ['POST', 'GET'])
def NextSite():#name , id):
    if request.method == "POST":
        title = request.form['title']
        intro = request.form['intro']
        text = request.form['text']

        article_for_db_setting = Article(title = title, intro = intro, TheText = text)  #создаём обьёкт который будем сеттить в bd

        try: #попытка сеттить в базу
            db.session.add(article_for_db_setting) # добавление в базу
            db.session.commit(); # применение изменений
            return redirect("/")# в случае успешного добавления, перенапрявлем на "/"

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
    articles = Article.query.order_by(Article.date).all()  # все записи в таблице, метод  order_by(Artcie.<поле модели) #вертает массив данных из бд
    return render_template("posts.html", articles=articles); # передача массива для дальнейшего отображения массива в шаблон
