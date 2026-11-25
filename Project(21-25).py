# Student Records Manager
user = input("Username: ")
password = input("Password: ")
if user == ("admin49%uni?+") and password == ("Blackb0X45#"):
    print("Access granted")
    
    data =[]   
    data.append({"Name": "Jake", "Course":"INS 211", "Test score": 78, "Exam score": 83, "Overall Score": 81.5, "Grade": "A"})
    data.append({"Name": "Henry", "Course":"CYB 201", "Test score": 85, "Exam score": 77, "Overall Score": 79.4, "Grade": "B"})
    data.append({"Name": "Robin", "Course":"COS 201", "Test score": 90, "Exam score": 94, "Overall Score": 92.8, "Grade": "A"})
    data.append({"Name": "Trish", "Course":"BIO 200", "Test score": 75, "Exam score": 80, "Overall Score": 78.5, "Grade": "B"})
    data.append({"Name": "Chris", "Course":"PHY 211", "Test score": 95, "Exam score": 98, "Overall Score": 97.1, "Grade": "A"})
    data.append({"Name": "Damian", "Course":"CSC 203", "Test score": 88, "Exam score": 92, "Overall Score": 90.8, "Grade": "A"})
   
    
    student = input("Add new student,Yes or No?  ")
    if student == ("Yes"):
        stu_name = input("Student name: ")
        course = input("Name of Course:  ")  
        test_score = int(input("Test Score: "))
        exam_score = int(input("Exam score: "))
        def test(n1): 
            sub = n1 / 100
            first_score = sub * 30
            return first_score
        def exam(n2):
            sub = n2 / 100
            second_score = sub * 70
            return second_score
        # def calc():
        #     score = test(data[0:6]["Test score"]) + exam(data[0:6][0:6]["Exam score"])
           
        #     return  [{"Overall Score": score}]
        # calc()          
        def overall():
            final_score = test(test_score) + exam(exam_score)
            return final_score

        overall() 
        def grade():
            if (overall() >= 80) and (overall() <= 100):
                return "A"
            elif (overall() >= 70) and (overall() < 80):
                return "B"
            elif (overall() >= 50) and (overall() < 70):
                return "C"
            elif (overall() >= 40) and (overall() < 50):
                return "D"
            elif (overall() >= 20) and (overall() < 40):
                return "E"
            else: 
                return "F" 

            grade()                       
        data.append({"Name": stu_name, "Course": course,"Test score": test_score, "Exam score": exam_score, "Overall Score": overall(), "Grade": grade() })
    
    # info = {"Name":["Jake", "Henry", "Robin"],"Course":["Information Systems", "Cyber Security", "Computer Science"],"Score":[67, 81, 97]}
    
    for info in data:
        print(info)
else:
    print("Access denied")    