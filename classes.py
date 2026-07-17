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
        data = [student.__dict__ for student in self.students]

        with open(filename, 'w', encoding="utf-8") as f:
            json.dump(data, f, indent=4)


    def load_from_json(self, filename):
        try:
            with open(filename, 'r', encoding="utf-8") as f:
                data = json.load(f)
                self.students = []

                for student_dict in data:
                    student = Student(**student_dict)
                    self.students.append(student)
        except FileNotFoundError:
           print("No saved students found")
        except json.JSONDecodeError:
            print("The file is empty or contains invalid JSON.")

      
           

       





