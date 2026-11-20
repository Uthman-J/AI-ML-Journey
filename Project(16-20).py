# Student Records Manager
user = input("Username ")
password = input("Password ")
if user == ("admin49%uni?+") and password == ("Blackb0X45#"):
    print("Access granted")
    data =[]
    # info = {"Name":["Jake", "Henry", "Robin"],"Course":["Information Systems", "Cyber Security", "Computer Science"],"Score":[67, 81, 97]}
    data.append({"Name": "Jake", "Course":"Information Systems", "Score": 67 })
    data.append({"Name": "Henry", "Course":"Cyber Security", "Score": 81 })
    data.append({"Name": "Robin", "Course":"Computer Science", "Score": 97 })
    data.append({"Name": "Trish", "Course":"Biochemistry", "Score": 79 })
    data.append({"Name": "Chris", "Course":"Medicine", "Score": 99 })
    data.append({"Name": "Damian", "Course":"Computer Science", "Score": 97 })
    for info in data:
        print(info)
else:
    print("Access denied")    