from flask import Blueprint, request, redirect, url_for, flash, session
from .models import addUserToTable, checkUsername, getUserId, getUserInfo, changeName

auth = Blueprint(
    'auth',
    __name__,
    static_folder='static',
    template_folder='templates'
)


@auth.route('/signup', methods=['POST'])
def signup():
    if request.method == 'POST':
        name = request.form.get('signupName')
        username = request.form.get('signupAccount')
        password1 = request.form.get('signupPassword1')
        password2 = request.form.get('signupPassword2')
        if password1 == password2:
            if checkUsername(username):
                addUserToTable(name, username, password1)
                flash('帳號申請成功', 'success')

            else:
                return redirect('error/?message=帳號已經被註冊')
        else:
            flash('密碼確認不相符', 'error')

        return redirect(url_for('views.home'))


@auth.route('/signin', methods=['POST'])
def signin():
    if request.method == 'POST':
        userName = request.form.get('account')
        userPassword = request.form.get('password')

        if userName == '' or userPassword == '':
            return redirect('error/?message=帳號或密碼空白')

        user = getUserId(userName, userPassword)

        if user:
            session['username'] = user

            return redirect(url_for('views.member'))

        else:
            return redirect('error/?message=帳號或密碼輸入錯誤')



@auth.route('/signout')
def signout():
    session['username'] = None
    flash('帳號已登出', 'error')
    return redirect(url_for('views.home'))


@auth.route('/api/members')
def getUserJsonInfo():
    username = request.args.get('username')
    data = getUserInfo(username)
    return data

# delete all global and use session.get

@auth.route('/api/member', methods=['POST'])
def updateName():
    req = request.headers.get('Content-Type')
    if req == 'application/json':
        json = request.json
        newName = json['name']
        changeName(newName, session.get('username'))

        data = {"ok": True}
        return data
    else:
        data = {"error": True}
        return data
