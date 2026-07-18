from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
import os
import pymysql

pymysql.install_as_MySQLdb()


app = Flask(__name__)
# Use DATABASE_URL env var if provided, otherwise fall back to a local sqlite file
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DATABASE_URL', 'sqlite:///airline.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)


class users(db.Model):
    '''
    uid, uname, password
    '''
    uid = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(25), nullable=False)
    age = db.Column(db.Integer, nullable=False)
    email = db.Column(db.String(22), nullable=False)
    password = db.Column(db.String(20), nullable=False)


class bookings(db.Model):
    '''
    bid, username, arrival, departure
    '''
    bid = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(25), nullable=False)
    arrival = db.Column(db.String(50), nullable=False)
    departure = db.Column(db.String(50), nullable=False)


@app.route("/register", methods = ['GET', 'POST'])
def register():
    if request.method == 'POST':
        # Add entry to the database
        username = request.form.get('uname')
        age = request.form.get('age')
        email = request.form.get('email')
        password = request.form.get('password')

        entry = users(username=username, age=age, email=email, password=password)
        db.session.add(entry)
        db.session.commit()
        return redirect(url_for('login'))
    return render_template('booking.html')


@app.route("/login", methods = ['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form.get('uname')
        password = request.form.get('password')

        entry = users.query.filter_by(username=username, password=password).first()
        if entry:
            return redirect(url_for('booking'))
        else:
            return render_template('fail.html')
    return render_template('login.html')





@app.route("/booking", methods = ['GET', 'POST'])
def booking():
    if request.method == 'POST':
        
        username = request.form.get('uname') or request.form.get('username')
        arrival = request.form.get('arrival')
        departure = request.form.get('departure')

        entry = bookings(username=username, arrival=arrival, departure=departure)
        db.session.add(entry)
        db.session.commit()
        return render_template('successbook.html')
    return render_template('book_form.html')


@app.route("/")
def index():
    return render_template('login.html')


if __name__ == "__main__":
    # create DB tables if they don't exist
    with app.app_context():
        db.create_all()
    app.run(host="0.0.0.0", port=5000, debug=True)
