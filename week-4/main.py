from flask import Flask, render_template, request, session, redirect

app = Flask(
    __name__,
    static_folder="static",
    static_url_path="/"
)
app.secret_key = "superb5566"


class Users:
    def __init__(self):
        self.userAccount = None
        self.userPassword = None


admin = Users()
admin.userAccount = "test"
admin.userPassword = "test"


@app.route("/")
def home():
    return render_template('index.html')


@app.route("/signin", methods=["POST"])
def signin():
    session["userLogin"] = False

    if request.method == "POST":
        if session["userLogin"] is True:
            return redirect("/member/")
        else:
            userInputAccount = request.form["account"]
            userInputPassword = request.form["password"]

            if userInputAccount == admin.userAccount and userInputPassword == admin.userPassword:
                session["userLogin"] = True
                return redirect("/member/")
            elif userInputAccount is "" or userInputPassword is "":
                messageText = "請輸入帳號、密碼"
                return redirect(f"/error/?message={messageText}")
            else:
                messageText = "帳號、或密碼輸入錯誤"
                return redirect(f"/error/?message={messageText}")


@app.route("/member/")
def member():
    if session["userLogin"] is True:
        return render_template("/member.html")
    else:
        return redirect("/")


@app.route("/error/")
def error():
    data = request.args.get("message")
    return render_template("/error.html", data=data)


@app.route("/signout")
def signout():
    session["userLogin"] = False
    return redirect("/")


app.run(port=3000)

