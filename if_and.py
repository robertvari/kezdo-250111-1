email = "csaba@gmail.com"
password = "testpas123"

user_email = input("Email: ")
user_password = input("Password: ")

if user_email == email and user_password == password:
    print("You are logged in.")
else:
    print("Email or password is not correct.")