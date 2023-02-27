import requests
from flask import Flask, render_template, request, redirect
import psycopg2

app = Flask(__name__)

conn = psycopg2.connect(
    database="service_db",
    user="postgres",
    password="1",
    host="localhost",
    port="5432"
)

cursor = conn.cursor()


@app.route('/login/', methods=['GET'])
def index():
    return render_template('login.html')


@app.route('/login/', methods=['POST', 'GET'])
def login():
    if request.method == 'POST':
        if request.form.get("login"):
            username = request.form.get('username')
            password = request.form.get('password')
            cursor.execute("SELECT * FROM service.users WHERE login=\'{0}\' AND password=\'{1}\';".format(str(username),
                                                                                                          str(password)))
            if username == '' or password == '':
                return render_template("empty_login.html")
            records = list(cursor.fetchall())

            if records == []:
                return render_template("account_not_exists.html")

            return render_template('account.html', full_name=records[0][1], username=records[0][2],
                                   password=records[0][3])

        elif request.form.get("registration"):
            return redirect("/registration/")

    return render_template('login.html')


@app.route('/registration/', methods=['POST', 'GET'])
def registration():
    if request.method == 'POST':
        name = request.form.get('name')
        login = request.form.get('login')
        password = request.form.get('password')

        cursor.execute('SELECT * FROM service.users WHERE login=\'{0}\''.format(str(login)))
        record = list(cursor.fetchall())
        if record:
            return render_template('username_exist.html')
        else:
            if (login and password and name) and (login.count(' ') == 0 and password.count(' ') == 0
                                                  and name.count(' ') == 1 and name.find(' ') != 0 and name.find(
                        ' ') != (len(name) - 1)):

                cursor.execute(
                    'INSERT INTO service.users (full_name, login, password) VALUES (\'{0}\', \'{1}\', \'{2}\');'.format(
                        str(name), str(login), str(password)))


            else:
                return render_template('incorrect_reg_date.html')
            conn.commit()

        return redirect('/login/')

    return render_template('registration.html')