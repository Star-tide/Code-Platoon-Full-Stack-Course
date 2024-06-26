from flask import jsonify
from models import Students

#turn Students.query.all into a dict, so we can jsonify it when needed
student_data = [stud.to_dict() for stud in Students.query.all()]

