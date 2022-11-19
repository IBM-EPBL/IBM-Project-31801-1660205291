from flask import Flask, render_template, request, redirect, url_for, session
import ibm_db
import re


app = Flask(__name__)
  
app.secret_key = 'a'

conn = ibm_db.connect("DATABASE=bludb;HOSTNAME=54a2f15b-5c0f-46df-8954-7e38e612c2bd.c1ogj3sd0tgtu0lqde00.databases.appdomain.cloud;PORT=32733;SECURITY=SSL;SSLServerCertificate=Certificate.crt;UID=WJR97330;PWD=LyIGvWljvyXnJEUy",'','')

@app.route('/')

def homer():
    return render_template('index.html')


@app.route('/login',methods =['GET', 'POST'])
def login():
    global userid
    msg = ''
   
  
    if request.method == 'POST' :
        email = request.form['email']
        password = request.form['password']
        sql = "SELECT * FROM user WHERE email =? AND password=?"
        stmt = ibm_db.prepare(conn, sql)
        ibm_db.bind_param(stmt,1,email)
        ibm_db.bind_param(stmt,2,password)
        ibm_db.execute(stmt)
        account = ibm_db.fetch_assoc(stmt)
        print (account)
        if account:
            session['loggedin'] = True
            session['id'] = account['EMAIL']
            userid=  account['EMAIL']
            session['email'] = account['EMAIL']
            msg = 'Logged in successfully !'
            return render_template('dashboard.html', msg = msg)
        else:
            msg = 'Incorrect username / password !'
    return render_template('login.html', msg = msg)

        

   
@app.route('/signup', methods =['GET', 'POST'])
def register():
    msg = ''
    if request.method == 'POST' :
        name = request.form['name']
        email = request.form['email']
        phone = request.form['phone']
        password = request.form['password']
        sql = "SELECT * FROM user WHERE email =?"
        stmt = ibm_db.prepare(conn, sql)
        ibm_db.bind_param(stmt,1,email)
        ibm_db.execute(stmt)
        account = ibm_db.fetch_assoc(stmt)
        print(account)
        if account:
            msg = 'Account already exists !'
        elif not re.match(r'[^@]+@[^@]+\.[^@]+', email):
            msg = 'Invalid email address !'
        elif not re.match(r'[A-Za-z0-9]+', name):
            msg = 'name must contain only characters and numbers !'
        else:
            insert_sql = "INSERT INTO  user VALUES (?, ?, ?, ?)"
            prep_stmt = ibm_db.prepare(conn, insert_sql)
            ibm_db.bind_param(prep_stmt,1,name)
            ibm_db.bind_param(prep_stmt,2,email)
            ibm_db.bind_param(prep_stmt,3,phone)
            ibm_db.bind_param(prep_stmt,4,password)
            ibm_db.execute(prep_stmt)
            msg = 'You have successfully registered !'
    elif request.method == 'POST':
        msg = 'Please fill out the form !'
    return render_template('signup.html', msg = msg)

@app.route('/dashboard')
def dash():
    return render_template('dashboard.html')

@app.route('/apply',methods =['GET', 'POST'])
def apply():
     msg = ''
     if request.method == 'POST' :
         job = request.form['job']
         name = request.form['name']
         email= request.form['email']
         qualification= request.form['qualification']
         skills = request.form['skills']
         youare = request.form['youare']
         experience = request.form['experience']
         sql = "SELECT * FROM user WHERE username =?"
         



         '''stmt = ibm_db.prepare(conn, sql)
         #ibm_db.bind_param(stmt,1,username)
         ibm_db.execute(stmt)
         account = ibm_db.fetch_assoc(stmt)
         print(account)
         #if account:
           # msg = 'there is only 1 job position! for you'
           # return render_template('apply.html', msg = msg)'''

         
         insert_sql = "INSERT INTO  jobs VALUES (?, ?, ?, ?, ?, ?, ?)"
         prep_stmt = ibm_db.prepare(conn, insert_sql)
         ibm_db.bind_param(prep_stmt, 1, job)
         ibm_db.bind_param(prep_stmt, 2, name)
         ibm_db.bind_param(prep_stmt, 3, email)
         ibm_db.bind_param(prep_stmt, 4, qualification)
         ibm_db.bind_param(prep_stmt, 5, skills)
         ibm_db.bind_param(prep_stmt, 6, youare)
         ibm_db.bind_param(prep_stmt, 7, experience)
         ibm_db.execute(prep_stmt)
         msg = 'You have successfully applied for job !'
         session['loggedin'] = True
        #  TEXT = "Hello sandeep,a new appliaction for job position" +jobs+"is requested"

     elif request.method == 'POST':
         msg = 'Please fill out the form !'
     return render_template('apply.html', msg = msg)



@app.route('/display')
def display():
    print(session["email"],session['id'])
    
    cursor = mysql.connection.cursor()
    cursor.execute('SELECT * FROM jobs WHERE userid = % s', (session['id'],))
    account = cursor.fetchone()
    print("accountdislay",account)

    return render_template('display.html',account = account)


@app.route('/logout')

def logout():
   session.pop('loggedin', None)
   session.pop('id', None)
   session.pop('email', None)
   return render_template('index.html')


    
if __name__ == '__main__':
   app.run(host='0.0.0.0')