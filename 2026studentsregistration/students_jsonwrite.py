

import json
import os

FILE_NAME= "students.json"

def load_students():
    if os.path.exists(FILE_NAME):
        with open(FILE_NAME,"r") as file:
            try:
                return json.load(file)
            except json.decoder.JSONDecodeError:
                return []
    return []

# json.dump(file,
def save_students():
    with open(FILE_NAME,"w") as file:
        json.dump(students,file,indent=4)


students = load_students() # List

# name = input("Enter your name: ").strip()
# Mobile = input("Enter your Mobile: ").strip()
# location = input("Enter your Location: ").strip()


def getlocation():
    location = input("Enter your Location: ").strip()
    if location.isnumeric():
        print("Please enter a valid number")
        return location
    else:
        print("Please enter a valid number")
        location = input("Enter your Location: ").strip()
        return location


def getmobile():
    mobile = input("Enter your Mobile: ").strip()

    if mobile.isdigit():
        mobile = int(mobile)
        return mobile
    else:
        print("Please enter a valid mobile number.")

def getvalidname():
    name= input("enter your nane: ").strip()

    if name.isalpha():
        return name
    else:
        print("invalid name")

def getvalidemail():
    email= input("enter proper email: ").strip()
    if "@" in email or "." in email:
        return email
    else:
        print("invalid email")

def add_student():
    print ("\n --student registration")

    student={"Name":getvalidname(),"Mobile":getmobile(),"Location":getlocation(),"Email":getvalidemail()}
    students.append(student)
    save_students()
    print ("\n --student registration successfully")

def view_student():
    print("\n --student List")
    if not students:
        print("No students")
        return
    for i in students:
        print(f"Name: {i['Name']},Mobile: {i['Mobile']}, Location:{i['Location']}")

def main():
    while True:
        print("\n --student registration")

        print("1. Add student")
        print("2. View student")
        print("3. Exit")

        choice = input("Enter your choice: ").strip()
        if choice == "1":
            add_student()
        elif choice == "2":
            view_student()
        elif choice == "3":
            print("exiting registration")
            exit()
        else:
            print("Invalid choice")
if __name__ == "__main__":
    main()



# using choice to determine which method to take
# if not students: since we define as empty list