from flask import Flask, render_template,session,redirect, url_for, escape, request
import re
import sqlite3 as sql
import time
import os

app = Flask(__name__)

# MAIN ROUTE
@app.route('/')
def homepage():
    return render_template('routes.html')

# ADMIN REGISTER PAGE
@app.route('/admin/register')
def aregister():
    return render_template('aregister.html')

# ADMIN LOGIN PAGE
@app.route('/admin/login')
def asignin():
    return render_template('alogin.html',status=1)

# ADMIN LOGIN DASHBOARD
@app.route('/admin/login',methods=['POST'])
def alogin():
    email = request.form['user_email']
    pwd = request.form['user_password']
    with sql.connect("database.db") as con:
        cur = con.cursor()
        cur.execute("SELECT * FROM ADMIN WHERE name IS (?) AND password IS (?) LIMIT 1",(email,pwd))
        try:
            [(w,x,y,z)]=cur.fetchall()
            session['user']='admin'
            session['level']=x
            session['username']=y
        except ValueError:
            return render_template('alogin.html',status=0)
    return render_template('data.html')

# ADMIN SUBMIT PAGE
@app.route('/admin/submit',methods=['POST'])
def asubmit():
    name = request.form['user_name']
    email = request.form['user_email']
    pwd = request.form['user_password']
    with sql.connect("database.db") as con:
        cur = con.cursor()
        cur.execute("INSERT INTO ADMIN (admin_level,name,password) VALUES (?,?,?)",(0,name,pwd))
        con.commit()
    return redirect(url_for('adashboard'))

# ADMIN DASHBOARD
@app.route('/admin/dashboard')
def adashboard():
    try: 
        if(session['user'] == 'admin'):
            render_template('data.html')
        else: 
            return redirect(url_for('asignin'))
    except KeyError:
        return redirect(url_for('asignin'))
    return redirect(url_for('asignin'))

# ADMIN COMPLAIN PAGE
@app.route('/admin/complain')
def complainAll():
    if(session['user'] == 'admin'):
        con = sql.connect("database.db")
        con.row_factory = sql.Row
        cur = con.cursor()
        cur.execute("SELECT * from COMPLAIN")
        rows = cur.fetchall()
        print(rows)
        return render_template("clist.html",rows = rows)
    else:
        redirect(url_for('asignin'))

# ADMIN USER PAGE
@app.route('/admin/users')
def ausers():
    con = sql.connect("database.db")
    con.row_factory = sql.Row
    cur = con.cursor()
    cur.execute("SELECT * from USER")
    rows = cur.fetchall()
    
    return render_template("ulist.html",rows = rows,adminlevel=session['level'])

# COMPLAIN PORTAL
@app.route('/portal/complain')
def complainp():
    return render_template("cop.html")

# COMPLAIN REQ
@app.route('/usubmit',methods=['POST'])
def submit():
    body = request.form["complain"]
    cat = request.form.get("cat")
    print(cat)
    with sql.connect("database.db") as con:
        cur = con.cursor()
        cur.execute("INSERT INTO COMPLAIN (body,category,status_id,time_stamp) VALUES (?,?,?,?)",(body,cat,0,time.time()))
        con.commit()
        msg = "Record successfully added"
    return redirect(url_for('homepage'))

if __name__ == '__main__':
    app.secret_key=os.urandom(24)
    app.run(debug=True, use_reloader=True)
