class Student:
    def __init__(self, name, roll_no, marks):
        self.name = name
        self.roll_no = roll_no
        self.marks = marks
    def display_info(self):
        print(f"Name: {self.name} | Roll_no: {self.roll_no} | Marks: {self.marks}")

    def get_grade(self):
        if self.marks >= 90:
            print("Grade A ")
        elif self.marks >= 75:
            print("Grade B")
        elif self.marks >= 65:
            print("Grade C")
        elif self.marks >=55:
            print("Grade D")
        elif self.marks >= 40:
            print("Pass")
        elif self.marks >= 35:
            print("Just Pass")    
        else:
            print("fail")      
Student_list = []
while True:
    print("\n_ _ _ STUDENT MANAGEMENT SYSTEM _ _ _")
    print("1. Add Student")
    print("2. View All Student")
    print("3. Search Student by Roll No")
    print("4. Exit")

    choice = input("Enter your choice (1-4): ")
    if choice == "1":
        # 1. user se 3 input lo:
        name = input("Enter student name: ")
        roll_no = int(input("Enter roll number: "))
        marks = int(input("Enter marks: "))

        # 2. student class ka naya object banao:
        s = Student(name, roll_no, marks)

        # 3. list me append:
        Student_list.append(s)

        print("Student added successfully! ")
    elif choice == "2":
        if len(Student_list) == 0:
            print("there no student added")    
        else:
            print("\n--- ALL STUDENT LIST---")
            for s in Student_list:
                s.display_info() 
                s.get_grade()
    elif choice == "3":
        search_roll = int(input("Enter roll number to search: "))
        found = False

        for s in Student_list:
            if s.roll_no == search_roll:
                print("\nStudent Mil Gaya! ✅")
                s.display_info()
                s.get_grade()
                found = True
                break

        if found == False:
            print("Student nahi mila is roll number se! ❌")            
    elif choice == "4":
        print("thank you! Progran closing....")
        break
    else:
        print("Invalid choice! kripya 1, 2, 3 ya 4 hii daalein. ")             