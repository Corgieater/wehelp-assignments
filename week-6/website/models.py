# models is a place to interact with database
from flask import Blueprint
from .__init__ import mydb, mycursor
from flask_bcrypt import Bcrypt

models = Blueprint(
    'models',
    __name__
)

bcrypt = Bcrypt()

def createTable():
    mycursor.execute('select table_schema as database_name, '
                   'table_name from information_schema.tables where table_name = "member2";')
    searchTable = mycursor.fetchone()
    if searchTable is None:  #if the table exists, do not create it again
        mycursor.execute('CREATE TABLE `member2` (`id` INT PRIMARY KEY AUTO_INCREMENT,'
                       '`name` VARCHAR(255) NOT NULL UNIQUE,'
                       '`username` VARCHAR(255) NOT NULL UNIQUE,'
                       '`password` VARCHAR(255) NOT NULL)')
    mydb.commit()


def addUserToTable(name, username, password):
    insertExecution = ('INSERT INTO member2 values(DEFAULT, %s, %s, %s)')
    hashedPassword = bcrypt.generate_password_hash(password=password)  # encoding
    userInput = (name, username, hashedPassword)  # save encoded password in database
    mycursor.execute(insertExecution, userInput)
    mydb.commit()


def checkUsername(username):
    searchExecution = ('SELECT username FROM member2 WHERE username = %s')
    username = (username,) # 這逗點很重要, 因為資料型態一定要是tuple, 只有一個也要逗點
    mycursor.execute(searchExecution, username)

    searchResult = mycursor.fetchone()
    if searchResult is None:
        return True
    else:
        return False


def getUserId(username, password):  # for checking and returning user ID
    searchUsername = ('SELECT password FROM member2 WHERE username = %s')  # find hashed password by uername
    mycursor.execute(searchUsername, (username,))
    hashedPassword = mycursor.fetchone()
    if hashedPassword != None:
        hashedPassword = hashedPassword[0]
        checkPassword = bcrypt.check_password_hash(hashedPassword, password)
        # check if hashed password and user input are the same
    else:
        return False

    if checkPassword is True:
        searchExecution = ('SELECT name FROM member2 WHERE username = %s')
        mycursor.execute(searchExecution, (username,))
        searchResult = mycursor.fetchone()
        searchResult = searchResult[0]
        return searchResult
    else:
        return False
