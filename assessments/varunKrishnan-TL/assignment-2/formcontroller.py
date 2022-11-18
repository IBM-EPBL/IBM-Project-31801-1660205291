from flask import Flask, render_template, request
from werkzeug.utils import secure_filename
app = Flask(__name__)



@app.route('/')
def home():
    return render_template("allinone.html")

@app.route('/register', methods = ['GET',"POST"])
def login():
    if request.method == "POST":
        name = request.form["name"]
        phone = request.form["phone"]
        email = request.form["email"]
        skills = request.form["skills"]
        exp = request.form["exp"]
        f = request.files['file']
        f.save(secure_filename(f.filename))
        
        message = name + " -- " + email + " -- " + phone + " -- " + exp + " -- " + phone + "--- Your file uploaded successfully"
        
        # return render_template("index.html", y = name + " is pursing " + qualification +". He is " + age +" years old. His mail address is"+ email)
        return render_template("allinone.html", y = message )
        # return "File uploaded successfully"
        

if __name__ == "__main__":
    app.run(debug = True)
    
    
    