stu_name = input("Student name: ")
score = int(input("Score: "))
attendance = int(input("Attendance: "))
if (60 < score <= 100 and 50 < attendance <= 100):
    print(f"{stu_name}: Excellent")
elif (score >= 40 and 30 <= attendance <= 50) or (60 <= score <= 100 and attendance < 30 ) or (score >= 40 and 50 < attendance <= 100):
    print(f"{stu_name}: Pass")
elif (score > 100 and attendance >100) or (score < 0 and attendance < 0):
    print("Scores and attendance must be between 0 and 100")
else:
    print(f"{stu_name}: Fail")