class Student:

    def __init__(self, name, age, grade):

        self._name = name
        self._age = age
        self._grade = grade

    def __str__(self):
        return(f'Name: {self._name} \nAge: {self._age} \nGrade: {self._grade}th')
    
    def get_name(self):
        return self._name
    
    def get_age(self):
        return self._age
    
    def get_grade(self):
        return self._grade
    
    def set_name(self, name):
        if name.istitle() != False:
            return 'Name must be capitalized'
        if name.isalpha() == False:
            return 'Name must contain no digits, or special characters'
        self._name = name

    def set_age(self, age):
        if type(age) == int:
            if age > 11 and age < 18:
                self._age = age

    def set_grade(self, grade):
        if grade >= 9 and grade <= 12:
            self._grade = grade
    
    def advance(self):
        self._grade += 1
        return f'{self._name} has advanced to the {self._grade}th grade'

    def study(self):
        return f'{self._name} is studying Biology'
    
student_1 = Student('Brandon', 10, 5)
print(student_1)
student_1.set_name('BRENDAN')
student_1.set_age(30)
student_1.set_age(12)
student_1.set_name('48945')
student_1.set_name('Breanseon')
student_1.set_grade(9)


print(student_1.study())
print(student_1.advance())
print(student_1)