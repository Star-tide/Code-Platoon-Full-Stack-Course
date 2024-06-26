from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from models import db, Students, Teachers, Subjects
from flask import render_template

app = Flask('School API')
app.config['SQLALCHEMY_DATABASE_URI'] = "postgresql+psycopg://bnesslage@localhost:5432/school_api"
db.init_app(app)


@app.route('/')
def home_page():
    return render_template('base.html')

@app.route('/students')
def student_page():
    return render_template("students.html", students = Students.get_all_students())

@app.route('/subjects')
def subject_page():
    return render_template("subjects.html", subjects = Subjects.get_all_subjects())

@app.route('/teachers')
def teache_page():
    return render_template("teachers.html", teachers = Teachers.get_all_teachers())

app.run(debug=True)