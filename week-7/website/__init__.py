from flask import Flask
import mysql.connector
from mysql.connector import pooling

connectionPool = mysql.connector.pooling.MySQLConnectionPool(
    pool_name='myPool',
    pool_size=3,
    pool_reset_session=True,
    host='localhost',
    user='root',
    password='123456',
    database='website'
)
connection = connectionPool.get_connection()
mycursor = connection.cursor()


def createApp():
    app = Flask(
        __name__,
        static_folder='static',
        template_folder='templates'
    )
    app.config['SECRET_KEY'] = '55667788'
    app.config['JSON_AS_ASCII'] = False
    from .views import views
    from .auth import auth

    app.register_blueprint(views)
    app.register_blueprint(auth)

    return app
