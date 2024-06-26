from flask_sqlalchemy import SQLAlchemy
from flask import jsonify


#Creates a database instance, referencing school_api DB in postgresql
db = SQLAlchemy()

class Students(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(50))
    last_name = db.Column(db.String(50))
    age = db.Column(db.Integer)
    subject = db.Column(db.String(50))

    @classmethod
    def get_all_students(cls):
        student_data = [stud.to_dict() for stud in Students.query.all()]
        return student_data
    
    def to_dict(self):
        return {
            "id":self.id,
            "first_name":self.first_name,
            "last_name":self.last_name,
            "age":self.age,
            "grade":self.subject
        }
    
class Subjects(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    subject = db.Column(db.String(50))
    

    @classmethod
    def get_all_subjects(cls):
        subject_data = [subject.to_dict() for subject in cls.query.all()]
        return subject_data

    def to_dict(self):
        return {
            "id":self.id,
            "subject":self.subject
        }
    
class Teachers(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(50))
    last_name = db.Column(db.String(50))
    age = db.Column(db.Integer)
    subject = db.Column(db.String(50))

    @classmethod
    def get_all_teachers(cls):
        teacher_data = [teacher.to_dict() for teacher in cls.query.all()]
        return teacher_data

    def to_dict(self):
        return {
            "id":self.id,
            "first_name":self.first_name,
            "last_name":self.last_name,
            "age":self.age,
            "subject":self.subject
        }