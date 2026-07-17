import json
from data import Student

class Student_Manager:
    def __init__(self):
        self.students = [] 

    def add_student(self, name, student_id, grade):
        temp = Student(name, student_id, grade)
        self.students.append(temp)

    def show_student(self):
        for student in self.students:
            print(student.name)
            print(student.student_id)
            print(student.grade)
            print("\n\n")
    
    def search_student(self, id):
        for student in self.students:
            if student.student_id == id:
                print(student.name)
                print(student.grade)
        
        print("Nothing found")
    
    def delete_student(self, id):
        i = 0
        for student in self.students:
            i = i + 1
            if student.student_id == id:
                del self.students(i)
                return

        print("No such student is enrolled")
        
            
    def save_to_json(self, filename):
        with open(filename, 'w') as f:
            f.write(json.dumps(self.students, indent=4))
        

    def load_from_json(self, filename):
        print("I've got no clue")
       





