from flask import Flask, render_template, flash, request, session
from flask import render_template, redirect, url_for, request
import mysql.connector



app = Flask(__name__)
app.config['DEBUG']
app.config['SECRET_KEY'] = '7d441f27d441f27567d441f2b6176a'



@app.route("/")
def homepage():
    return render_template('index.html')









@app.route("/AdminLogin")
def AdminLogin():
    return render_template('AdminLogin.html')

@app.route("/UserLogin")
def UserLogin():
    return render_template('UserLogin.html')

@app.route("/NewUser")
def NewUser():
    return render_template('NewUser.html')


@app.route("/In")
def In():
    return render_template('In.html')

@app.route("/Out")
def Out():
    return render_template('Out.html')

@app.route("/AdminHome")
def AdminHome():

    conn = mysql.connector.connect(user='root', password='', host='localhost', database='1vehicleParkdb')
    cur = conn.cursor()
    cur.execute("SELECT * FROM regtb ")
    data = cur.fetchall()

    return render_template('AdminHome.html', data=data)

@app.route("/AdminReport")
def AdminReport():


    conn = mysql.connector.connect(user='root', password='', host='localhost', database='1vehicleParkdb')
    cur = conn.cursor()
    cur.execute("SELECT * FROM entrytb  ")
    data = cur.fetchall()
    return render_template('AdminReport.html', data=data)



@app.route("/adminlogin", methods=['GET', 'POST'])
def adminlogin():
    error = None
    if request.method == 'POST':

       if request.form['Name'] == 'admin' and request.form['Password'] == 'admin':
           conn = mysql.connector.connect(user='root', password='', host='localhost', database='1vehicleParkdb')

           cur = conn.cursor()
           cur.execute("SELECT * FROM regtb ")
           data = cur.fetchall()


           return render_template('AdminHome.html', data=data)

       else:
           data = "UserName or Password Incorrect!"

           return render_template('goback.html', data=data)






@app.route("/newuser", methods=['GET', 'POST'])
def newuser():
     if request.method == 'POST':

          name = request.form['t1']

          mobile = request.form['t2']
          email = request.form['t3']
          vno = request.form['t6']
          username = request.form['t4']
          Password = request.form['t5']

          conn = mysql.connector.connect(user='root', password='', host='localhost', database='1vehicleParkdb')
          cursor = conn.cursor()
          cursor.execute("insert into regtb values('','"+name+"','"+mobile+"','"+email+"','"+vno +"','"+username+"','"+Password+"')")
          conn.commit()
          conn.close()

     data = "Record Saved!"

     return render_template('goback.html', data=data)




@app.route("/userlogin", methods=['GET', 'POST'])
def userlogin():

    if request.method == 'POST':
        username = request.form['Name']
        password = request.form['Password']
        #session['uname'] = request.form['uname']

        conn = mysql.connector.connect(user='root', password='', host='localhost', database='1vehicleParkdb')
        cursor = conn.cursor()
        cursor.execute("SELECT * from regtb where username='" + username + "' and Password='" + password + "'")
        data = cursor.fetchone()
        if data is None:

            alert = 'Username or Password is wrong'
            return render_template('goback.html', data=alert)



        else:

            session['uname'] = data[4]
            conn = mysql.connector.connect(user='root', password='', host='localhost', database='1vehicleParkdb')
            # cursor = conn.cursor()
            cur = conn.cursor()
            cur.execute("SELECT * FROM regtb where username='" + username + "' and Password='" + password + "'")
            data = cur.fetchall()

            return render_template('UserHome.html', data=data )


@app.route("/UserHome")
def UserHome():
    username = session['uname']

    conn = mysql.connector.connect(user='root', password='', host='localhost', database='1vehicleParkdb')
    cur = conn.cursor()
    cur.execute("SELECT * FROM regtb  where username='" + username + "' ")
    data = cur.fetchall()
    return render_template('UserHome.html', data=data)



@app.route("/UserReport")
def UserReport():
    username = session['uname']

    conn = mysql.connector.connect(user='root', password='', host='localhost', database='1vehicleParkdb')
    cur = conn.cursor()
    cur.execute("SELECT * FROM entrytb  where VehicleNo='" + username + "' ")
    data = cur.fetchall()
    return render_template('UserReport.html', data=data)



@app.route("/vin", methods=['GET', 'POST'])
def vin():

    if request.method == 'POST':
        vno = request.form['vno']

        import datetime

        date = datetime.datetime.now().strftime('%d-%b-%Y')

        status = '0'

        conn = mysql.connector.connect(user='root', password='', host='localhost', database='1vehicleParkdb')
        cursor = conn.cursor()
        cursor.execute("SELECT * from regtb where VehicleNo='" + vno + "'")
        data = cursor.fetchone()
        if data is None:

            alert = 'VehicleNo Not Register '
            return render_template('goback.html', data=alert)

        else:

            for x in range(1, 21):
                print(x)



                conn = mysql.connector.connect(user='root', password='', host='localhost', database='1vehicleParkdb')
                cursor = conn.cursor()
                cursor.execute("SELECT * from entrytb where   Date='" + date + "' and Status='in'  and ParkingNo='" + str(x) + "' ")
                data = cursor.fetchone()
                if data is None:
                    conn = mysql.connector.connect(user='root', password='', host='localhost',
                                                   database='1vehicleParkdb')
                    cursor = conn.cursor()
                    cursor.execute(
                        "insert into entrytb values('','" + vno + "','" + date + "','in','" + str(x) + "')")
                    conn.commit()
                    conn.close()
                    status = '1'

                    return render_template('In.html', data=str(x))





            if status=="0":
                alert = 'Parking lot Full  '
                return render_template('goback.html', data=alert)






@app.route("/vout", methods=['GET', 'POST'])
def vout():

    if request.method == 'POST':
        vno = request.form['vno']

        import datetime

        date = datetime.datetime.now().strftime('%d-%b-%Y')

        conn = mysql.connector.connect(user='root', password='', host='localhost', database='1vehicleParkdb')
        cursor = conn.cursor()
        cursor.execute(
            "SELECT * from entrytb where vehicleno='" + vno + "' and Date='" + date + "' and Status='in'  ")
        data = cursor.fetchone()
        if data :
            conn = mysql.connector.connect(user='root', password='', host='localhost',
                                           database='1vehicleParkdb')
            cursor = conn.cursor()
            cursor.execute("update entrytb set Status='out' where vehicleno='" + vno + "' and Date='" + date + "' and Status='in'  ")
            conn.commit()
            conn.close()

            alert = ' vehicle out  '
            return render_template('goback.html', data=alert)

        else:
            alert = ' vehicle is not parking  '
            return render_template('goback.html', data=alert)


















if __name__ == '__main__':
    app.run(debug=True, use_reloader=True)