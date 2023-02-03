#IEBC
age=int(input("Enter your age: "))
citizenship=input("Enter citizenship: ")
countries="kenya,uganda,tanzania"
if (age>=18 and citizenship in countries):
    print("You are eligible to vote")
else:
    print("You are not eligible to vote")