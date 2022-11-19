from flask import *
app = Flask(__name__)


@app.route('/')
def setcookie():
    res = make_response("Cookie is set")
    res.set_cookie("device", "hp")
    res.set_cookie("name", "nandha")
    return res


if __name__ == "__main__":
    app.run(debug = True)