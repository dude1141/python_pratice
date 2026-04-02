students = []  # List

# {"Name":"Mahesh","Mobile":"8899663322",
#  "Email":"mahesh@gmail.com", "Location":"Hyd",
#  "Qualification":"BTech"}

students.append({"Name":"Mahesh","Mobile":"8899663322","Email":"mahesh@gmail.com", "Location":"Hyd","Qualification":"BTech"})

students.append({"Name":"Venkat","Mobile":"8009663322","Email":"venkat@gmail.com", "Location":"Hyd","Qualification":"MTech"})

students.append({"Name":"Pavan ","Mobile":"81199663322","Email":"pavan@gmail.com", "Location":"Hyd","Qualification":"MCA"})

students.append({"Name":"   Pavan","Mobile":"81199663322","Email":"pavan@gmail.com", "Location":"Hyd","Qualification":"Bpharm"})


#view students here
for i in students:
    print(f"Name: {i['Name']},Mobile: {i['Mobile']}, Location:{i['Location']}")

#search studnets

studentname= input("Enter your name: ").strip().lower()

found= False
for i in students:
    if i['Name'].lower().strip() == studentname:
        print("\n student found")
        found= True
        break
if not found:
    print("\n student not found")
    #found= False


