from classes import Student_Manager

manager = Student_Manager()

def get_input():
    while (True):
        try:
            temp = int(input("Enter your choice: "))
            if 0 < temp <= 7 :
                return temp
            else:
                print("Choice input must be from 1 to 7")
        except ValueError:
            print("Please enter a valid number")


def ask_for_id():
    while (True):
        student_id = input("Enter an ID: ")

        if student_id:
            return student_id
        else:
            print("you can't enter a empty input")

    
def ask_for_name():
    while(True):
        name = input("Enter a name: ")
        if name.isdigit():
            print("Please enter a valid name")
            name = None
        elif not name:
            print("Please enter a name")
        else:
            name = name.strip()
            return name


def ask_for_grade():
     while(True):
        try:
            grade = float(input("Enter a grade: "))

            if 0 <= grade <= 100:
                return grade
            else:
                print("Grade must be between 0 and 100.")
        except ValueError:
             print("Please enter a valid number.")



def show_menu():
    print("***** Student manager system *****")
    print("-" * 40)
    print("Please choose an action by entering their number of order: (1-7)")
    print("1.Add student")
    print("2.Show students")
    print("3.Search student")
    print("4.Delete student")
    print("5.Save")
    print("6.Load")
    print("7.Exit")

    choice = get_input()
            

    match choice:
        case 1:
            manager.add_student(ask_for_name(), ask_for_id(), ask_for_grade())
            return True
        case 2:
            manager.show_student()
            return True
        case 3:
            manager.search_student(ask_for_id())
            return True
        case 4:
            manager.delete_student(ask_for_id())
            return True
        case 5:
            manager.save_to_json("students.json")
            return True
        case 6:
            manager.load_from_json("students.json")
            return True
        case 7:
            print("Thank you for choosing our program!")
            manager.save_to_json("students.json")
            return False
        

def main():
    manager.load_from_json("students.json")
    while(True):
        if not show_menu():
            break
    
    
if __name__ == "__main__":
    main()




