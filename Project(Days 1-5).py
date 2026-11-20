# Age Calculator
birth = int(input("What year were you born?" ))
today = int(input("What year is it today?" ))
age = today - birth
print(f"You are {age} years old")
# Simple Calculator
val_1 = int(input("Input a number"))
val_2 = int(input("Input another number"))
operate = input(f"{val_1}__{val_2},  Enter an arithmetic operator")
if (operate == "+") or (operate == "addition") or(operate == "add") :
    result = val_1 + val_2
elif (operate == "-") or (operate == "subtraction") or (operate == "subtract"):
    result = val_1 - val_2
elif (operate == "*") or (operate == "multiplication") or (operate == "multiply"):
    result = val_1 * val_2
elif ((val_2 == 0) and (operate == "/")) or ((val_2 == 0) and (operate == "division")) or ((val_2 == 0) and (operate == "divide")):
    result = "undefined" 
elif (operate == "/") or (operate == "division") or (operate == "divide"):
    result = val_1 / val_2
elif (operate == "%") or (operate == "modulo"):
    result = val_1 % val_2
print(result)
# Temperature Converter
temp = input("What temperature is it?")
if (temp[-1] == "C") or (temp[-1] == "c"):
    val_1 = float(temp.replace(temp[-1], "")) 
    fah = val_1 * 1.8 + 32 
    print(f"{fah:.1f}F")
elif (temp[-1] == "F") or (temp[-1] == "f"):
    val_2 = float(temp.replace(temp[-1], "")) 
    celc = (val_2 - 32) / 1.8
    print(f"{celc:.1f}C")
else:
    print("Enter either C for Celcius or F for Fahrenheit")
#  Grade Checker
score = int(input("Input your score"))
if score >= 90:
    print("A")
elif score >= 80:
    print("B")
elif score >= 70:
    print("C")
elif score >= 60:
    print("D")
elif score < 60:
    print("F")
# Number Comparison
a = int(input("Input a number"))
b = int(input("Input another number"))
if a > b:
    print(f"{a} > {b} or {b} < {a}")
elif b > a:
    print(f"{b} > {a} or {a} < {b}")
elif a == b:
    print(f"{a} = {b}")