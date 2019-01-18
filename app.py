from flask import Flask, request, session, g, url_for, abort, render_template,make_response,redirect
import re
import flask_login
from mysql_db import MySQL

app = Flask(__name__)
app.debug = 1
app.config.from_pyfile('config.py')
mysql = MySQL(app)
application = app

'''@app.route("/")
def main():
    cursor = mysql.connection.cursor(named_tuple=True)
    cursor.execute('select count(*) as count from tbl_user')
    one_count = cursor.fetchone().count
    cursor.execute('select count(*) as count from db2')
    two_count = cursor.fetchone().count
    return one_count
    return two_count'''

@app.route('/')
def main(): pass

@app.route('/login', methods = ['GET', 'POST'])
def login():
    error = None
    if request.method == 'POST':
        if valid_login(request.form['username'], request.form['password'])
            searchword = request.args.get('key', '')
            return log_the_user_in(request.form['username'])
    else:
        error = "You invalid"
    return render_template('login.html', error = error)

@app.route('/user/<username>')
def profile(username): pass

with app.test_request_context():
  #print url_for('/')
  print url_for('login')
  print url_for('login', next='/')
  print url_for('profile', username='John Doe')

@app.route('/hello/')
@app.route('/hello/<name>')
def hello(name = None):
    return render_template('hello.html', name = name)

#Чтение cookies:
@app.route('/')
def index():
    username = request.cookies.get('username')
    # Чтобы не получить в случае отсутствия cookie ошибку KeyError
    # используйте cookies.get(key) вместо cookies[key]
#Сохранение cookies:
@app.route('/')
def index():
    resp = make_response(render_template(...))
    resp.set_cookie('username', 'the username')
    return resp

if __name__ == "__main__":
    app.run()
