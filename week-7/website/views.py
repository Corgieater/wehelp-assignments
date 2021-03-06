from flask import Blueprint, render_template, session, redirect, url_for, request


views = Blueprint(
    'views',
    __name__,
    static_folder='static',
    template_folder='templates'
)


@views.route('/')
def home():
    return render_template('home.html')


@views.route('/member/') # do a dynamic route next time, make it multiple users
def member():
    if session['username']:
        return render_template('member.html', user=session['username'])
    else:
        return redirect(url_for('views.home'))


@views.route('/error/')
def errorPage():
    data = request.args.get("message")
    return render_template('error.html', data=data)
