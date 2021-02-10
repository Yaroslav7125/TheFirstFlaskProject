from flask import  Flask, render_template, url_for, request, redirect
from datetime import datetime
from flask_sqlalchemy import  SQLAlchemy
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

if __name__ == "__main__":
    app.run(debug=True);