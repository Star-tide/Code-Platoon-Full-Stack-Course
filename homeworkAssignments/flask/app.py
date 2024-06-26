from flask import Flask, jsonify
# from utils import all_students, old_students, young_students,advanced
from models import db, Students

app = Flask('Server')
app.config['SQLALCHEMY_DATABASE_URI'] = "postgresql+psycopg://bnesslage@localhost:5432/school_db"
db.init_app(app)

@app.route('/')
def home_page():
    return Students.get_all_students

@app.route('/raw_json/')
def raw_page():
    pass

@app.route('/advance_students/')
def advance_students():
     pass

@app.route('/old_students/')
def old_head():
    pass

@app.route('/young_students/')
def young_blood():
    pass

@app.route('/student_names/')
def names_students():
    pass

@app.route('/student_ages/')
def ages_students():
    pass

@app.route('/students/')
def students():
    pass


app.run(debug=True, port=8000)