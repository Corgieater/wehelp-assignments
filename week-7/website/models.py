from flask import Blueprint
from .__init__ import connection, mycursor
from flask_bcrypt import Bcrypt

models = Blueprint(
    'models',
    __name__
)

bcrypt = Bcrypt()

def addUserToTable(name, username, password):
    insertExecution = ('INSERT INTO member2 values(DEFAULT, %s, %s, %s)')
    hashedPassword = bcrypt.generate_password_hash(password=password)
    userInput = (name, username, hashedPassword)
    mycursor.execute(insertExecution, userInput)
    connection.commit()


def checkUsername(username):
    searchExecution = ('SELECT username FROM member2 WHERE username = %s')
    username = (username,)
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


def getUserInfo(username):  # return user info in json
    mycursor.execute('SELECT id, name, username FROM member2 WHERE username = %s', (username,))
    result = mycursor.fetchone()
    if result:
        data = {
            'data': {
                'id': result[0],
                'name': result[1],
                'username': result[2]
            }
        }
        return data
    else:
        data = {
            'data': None
        }
        return data


def changeName(newName, oldName):
    mycursor.execute('UPDATE member2 SET name = %s WHERE name = %s', (newName, oldName))
    connection.commit()
