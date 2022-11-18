from flask import Flask, render_template, request
app = Flask(__name__)


@app.route('/')
def home():
    return render_template("index.html")

@app.route('/login', methods = ["POST"])
def login():
    if request.method == "POST":
        name = request.form["name"]
        phone = request.form["phone"]
        email = request.form["email"]
        
        message = name + " --- " + email + " --- " + phone
        
        # return render_template("index.html", y = name + " is pursing " + qualification +". He is " + age +" years old. His mail address is"+ email)
        return render_template("index.html", y = message )

if __name__ == "__main__":
    app.run(debug = True)
    