# Number Counter
num = input("Input any numbers you want?")
count = 0
index = 0
while index < len(num):
    # num = int(num)
    draco = num[index].isdigit()
    if draco:
        count += 1
        index += 1
        # count += 1
        # index += 1
    else:
        # print("Input a number")
        # count += 1    
        index += 1
print(f"You inputed {count} digits") 
# Multiplication Table
n1 = int(input("Input a number"))
n2 = int(input("Input another number"))

if n2 > 0 and n1 > 0:
    for i in range(n2):
        order = i + 1
        mult = n1 * order
        print(f"{n1} * {order} = {mult}")
else:
    print("Input a positive number")
# sum calculator
no = int(input("Input a number"))
yes = int(input("Input another number"))
yeah = no + yes
print(f"{no} + {yes} = {yeah}")
# # guessing-style logic exercise
riddle = ("The person who invented me, didn't know me. The person who buys me doesn't need me. The person who uses me, doesn't see me. What am I?")
print(riddle)
while True:
    ans = input("")
    ans = ans.lower()
    if ans == "coffin":
        print("Correct, you're smart")
        break
    else:
        print("Try again")
# student-score processing 
score = int(input("Input your score"))
if score >= 90 and score <= 100:
    print("You're an A student")
elif score >= 70 and score < 90:
    print("You're a B student")
elif score >= 50 and score < 70:
    print("You're a C student")
elif score >= 30 and score < 50:
    print("You're a D student")
elif score >= 10 and score < 30:
    print("You're an E student")
elif score >= 0 and score < 10:
    print("You're a F student")
else:
    print("Your score must be within the range of 0-100")