from flask_sqlalchemy import SQLAlchemy
from flask import jsonify
db = SQLAlchemy()

# Models represent SQL table creation. Similar to templates. Have a class inherit db.Model in order to create new tables in python. This is possible with SQLAlchemy
class Students(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(50))
    last_name = db.Column(db.String(50))
    age = db.Column(db.Integer)
    grade = db.Column(db.String(1))

    @classmethod
    def get_all_students(cls):
        student_data = [stud.to_dict() for stud in cls.query.all()]
        return jsonify(student_data)

    def to_dict(self):
        return {
            "id":self.id,
            "first_name":self.first_name,
            "last_name":self.last_name,
            "age":self.age,
            "grade":self.grade
        }