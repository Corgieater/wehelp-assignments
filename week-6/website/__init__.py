from flask import Flask
import mysql.connector

mydb = mysql.connector.connect(
    host='localhost',
    user='root',
    password='123456',
    database='website',
)
mycursor = mydb.cursor()


def createApp():
    app = Flask(
        __name__,
        static_folder='static',
        template_folder='templates'
    )
    app.config['SECRET_KEY'] = '55667788'
    from .views import views
    from .auth import auth
    from .models import mydb, mycursor, createTable

    app.register_blueprint(views)
    app.register_blueprint(auth)

    createTable()
    return app
