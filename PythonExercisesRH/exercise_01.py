user_grade = int(input("Enter your grade (0-100): "))

if user_grade >= 90:
    print("Your grade is ")
elif user_grade >= 80:
    print("Your grade is B")
elif user_grade >= 70:
    print("Your grade is C")
elif user_grade >= 60:
    print("Your grade is D")
else:
    print("Your grade is F")
