# prajal mishra 1001434611
import os

from flask import Flask, request, render_template, Markup
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import create_engine
import time
import timeit
import psycopg2


APP = Flask(__name__)
APP.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

APP.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql+psycopg2://%s:%s@%s/%s' % (
    # ARGS.dbuser, ARGS.dbpass, ARGS.dbhost, ARGS.dbname
    'USERNAME', 'PASSWORD', 'URL', 'DATABASE'
)

# initialize the database connection
DB = SQLAlchemy(APP)

# initialize database migration management
MIGRATE = Migrate(APP, DB)

from models import *

db_string = 'postgresql+psycopg2://%s:%s@%s/%s' % (
    # ARGS.dbuser, ARGS.dbpass, ARGS.dbhost, ARGS.dbname
    'USERNAME', 'PASSWORD', 'URL', 'DATABASE'
)

db=create_engine(db_string)

@APP.route('/')
def view_registered_guests():
    guests = Guest.query.all()
    return render_template('guest_list.html', guests=guests)


@APP.route('/register', methods = ['GET'])
def view_registration_form():
    return render_template('guest_registration.html')


@APP.route('/register', methods = ['POST'])
def register_guest():
    # name = request.form.get('name') 
    course = request.form.get('old')
    section = request.form.get('zip')
    newname = request.form.get('newname')
    
    start=timeit.default_timer()
    
    # db.execute("UPDATE csefall2018 SET studentname=%s WHERE coursenumber=%s AND sectionnumber=%s",course,section,newname,course,section)
    result_set = db.execute("SELECT studentname,coursenumber FROM csefall2018 where coursenumber=%s",course)
    end=timeit.default_timer()
    timelapsed = end-start

    #SELECT zip, education FROM zipcodes_temp INNER JOIN education ON zipcodes_temp.city = education.City
    
    # for r in result_set:        
    #     if r.username == username and r.password == password:
    return render_template('guest_registration.html',
           result_set=result_set, timelapsed=timelapsed)
        # else:
    #         return render_template('guest_list.html',
    #         timelapsed=timelapsed)

@APP.route('/modify', methods = ['POST'])
def modify():
    
    username = request.form.get('old')
    password = request.form.get('zip')
    
    result_set = db.execute("SELECT username,password FROM students")
    result_set2 = db.execute("SELECT givenname,surname,streetadress FROM students where username=%s",username)
    # start=time.time()
    # db.execute("UPDATE zipcodes_temp SET state1=%s WHERE zip=%s", old,zip1)
    # result_set = db.execute("SELECT * FROM zip WHERE zip=%s",zip1)
    # end=time.time()
    for r in result_set:        
        if r.username == username and r.password == password:
            return render_template('modify.html',
           result_set=result_set, result_set2=result_set2)
        else:
            return render_template('modify.html')
    # timelapsed = end-start

    return render_template('modify.html',
        result_set=result_set, timelapsed=timelapsed)
    
@APP.route('/delete', methods = ['POST'])
def delete():
    
    delname = request.form.get('delname')
        
    start=time.time()
    db.execute("DELETE FROM zipcodes_temp WHERE zip=%s", delname)    
    end=time.time()
    
    timelapsed = end-start
    string1 = "Row Deleted!"
    return render_template('guest_list.html',
        string1=string1, timelapsed=timelapsed)

@APP.route('/barchart', methods = ['GET', 'POST'])
def barchart():
    values = db.execute("SELECT coursenumber, sum(maxenroll) as summ from csefall2018 group by coursenumber order by coursenumber")
    labels = db.execute("SELECT coursenumber, sum(maxenroll) as summ from csefall2018 group by coursenumber order by coursenumber")
    # labels = [
    #      'JAN', 'FEB', 'MAR', 'APR',
    #      'MAY', 'JUN', 'JUL', 'AUG',
    #      'SEP', 'OCT'
    # ]

    # values = [
    #      967.67, 1190.89, 1079.75, 1349.19,
    #      2328.91, 2504.28, 2873.83, 4764.87,
    #      4349.29, 6458.30
    # ]
    # colors = [
    # "#F7464A", "#46BFBD", "#FDB45C", "#FEDCBA",
    # "#ABCDEF", "#DDDDDD", "#ABCABC", "#4169E1",
    # "#C71585", "#FF4500", "#FEDCBA", "#46BFBD"]

    result_set = db.execute("SELECT * from csefall2018")
    return render_template('barchart.html', values=values, labels=labels, result_set=result_set, max=700)
    
@APP.route('/linechart', methods = ['GET', 'POST'])
def linechart():
    values = db.execute("SELECT totalpop from statevoting where totalpop between 500 and 800")
    labels = db.execute("SELECT voted from statevoting where totalpop between 500 and 800")
    # labels = [
    #      'JAN', 'FEB', 'MAR', 'APR',
    #      'MAY', 'JUN', 'JUL', 'AUG',
    #      'SEP', 'OCT'
    # ]

    # values = [
    #      967.67, 1190.89, 1079.75, 1349.19,
    #      2328.91, 2504.28, 2873.83, 4764.87,
    #      4349.29, 6458.30
    # ]
    colors = [
    "#F7464A", "#46BFBD", "#FDB45C", "#FEDCBA",
    "#ABCDEF", "#DDDDDD", "#ABCABC", "#4169E1",
    "#C71585", "#FF4500", "#FEDCBA", "#46BFBD"]

    result_set = db.execute("SELECT statename, totalpop, percentreg from statevoting where totalpop between 500 and 800")
    return render_template('linechart.html', values=values, result_set=result_set, max=1000)
    
@APP.route('/piechart', methods = ['GET', 'POST'])
def piechart():
    values = db.execute("SELECT coursenumber, sum(maxenroll) as summ from csefall2018  where maxenroll between 50 and 150 group by coursenumber order by coursenumber")
    labels = db.execute("SELECT coursenumber, sum(maxenroll) as summ from csefall2018 where maxenroll between 50 and 150 group by coursenumber order by coursenumber ")
    # labels = [
    #      'JAN', 'FEB', 'MAR', 'APR',
    #      'MAY', 'JUN', 'JUL', 'AUG',
    #      'SEP', 'OCT'
    # ]

    # values = [
    #      967.67, 1190.89, 1079.75, 1349.19,
    #      2328.91, 2504.28, 2873.83, 4764.87,
    #      4349.29, 6458.30
    # ]
    colors = [
    "#F7464A", "#46BFBD", "#FDB45C", "#FEDCBA",
    "#ABCDEF", "#DDDDDD", "#ABCABC", "#4169E1",
    "#C71585", "#FF4500", "#FEDCBA", "#46BFBD"]

    result_set = db.execute("SELECT statename, totalpop, percentreg from statevoting where totalpop between 500 and 800")
    return render_template('piechart.html', set=zip(values, labels, colors), result_set=result_set, max=100)
    