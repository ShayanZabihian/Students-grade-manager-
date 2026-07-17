class Student:
    def __init__(self, name, student_id, grade):

        if name.isdigit():
            raise ValueError("Value error")
        
        self.name = name

        self.student_id = student_id

        if 0 <= grade <= 100:
             self.grade = grade
        else:
            raise ValueError("Value error")