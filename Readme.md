#Flask project blog
*Для запуска проекта необходимо:*
    python runner.py "runserver" #start server - запустить каманду



*The desription's project* 

Все начинается с исполнения файла runner.py. Вторая строка в файле runner.py импортирует app и db из пакета app. Когда интерпретатор Python доходит до этой строки, управление программой передается файлу __init__.py, который в этот момент начинает исполняться. На 7 строке __init__.py импортирует модуль config, который передает управление config.py. Когда исполнение config.py завершается, управление снова возвращается к __init__.py. На 21 строке __init__.py импортирует модуль views, который передает управление views.py. Первая строка views.py снова импортирует экземпляр приложения app из пакета app. Экземпляр приложения app уже в памяти, поэтому снова он не будет импортирован. На строках 4, 5 и 6 views.py импортирует модели, формы и функцию send_mail и временно передает управление соответствующим файлам. Когда исполнение views.py завершается, управление программой возвращается к __init__.py. Это завершает исполнение __init__.py. Управление возвращается к runner.py и начинается исполнения инструкции на строке 3.

Третья строка runner.py импортирует классы, определенные в модуле models.py. Поскольку модели уже доступны в файле views.py, файл models.py не будет исполняться.

Поскольку runner.py работает как основной модуль, условие на 17 строке выполнено, и manager.run() запускает приложение.




python runner.py "runserver" #start server
python main2.py runserver  --host=127.0.0.2 --port 8000 #start server to current  port and api


-- creating data base
from apps import db #
db.create_all() #


            -- working with flask-script

