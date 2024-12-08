school = input("Hello! Which school you are from?")
print("What a great school!")

name = input("So what is your name?")
marks = input("what is your exam marks in maths this year?")
marks = int(marks)
if marks >= 80:
    grade = "A+"
    grade = str(grade)
    print("Academic excellence", name, "! Your grade is", grade)
elif marks >= 70:
    grade = "A"
elif marks >= 60:
    grade = "A-"
elif marks >= 50:
    grade = "B"
elif marks >= 40:
    grade = "C"
elif marks >= 30:
    grade = "D"
    print("Nice job! You got a ", grade)
else :
    grade = "F"
    print("Unfortunately, you got a", grade, name, "!")
