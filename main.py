from classes import Student_Manager

manager = Student_Manager()

def check_input(something):
    something = int(something)

    if something > 0 or something > 7:
        return False
    
    return True

def ask_for_id(name, student_id, grade):
    student_id = input("Enter an ID: ")
    return student_id

   

    
def ask_for_name():
    while(True):
        name = input("Enter a name: ")
        if name.isdigit():
            print("Please enter a valid name")
            name = None
        elif not name:
            print("Please enter a name")
        else:
            name = name.grim()
            return name

def ask_for_grade():
     while(True):
        grade = float(input("Enter a grade: "))
        if 0 < grade < 100:
            return grade




def show_menu():
    print("***** Student manager system *****")
    print("Please choose an action by entering their number of order:")
    print("1.Add student")
    print("2.Show students")
    print("3.Search student")
    print("4.Delete student")
    print("5.Save")
    print("6.Load")
    print("7.Exit")

    while(True):
        choice = input(" ")
        if check_input(choice):
            choice = int(choice)
            break

    match choice:
        case 1:
            manager.add_student(ask_for_name(), ask_for_id(), ask_for_grade())
        case 2:
            manager.show_student()
        case 3:
            manager.search_student(ask_for_id())
        case 4:
            manager.delete_student(ask_for_id())
        case 5:
            manager.save_to_json()
        case 6:
            manager.load_from_json()
        case 7:
            return 


    




    




