# user and password
a = "ak"
b = "111"
user = input("Enter user name: ")
if user==a:
    password = input("Enter password: ")
    if password==b:
        print("WELCOME")
    else:
        print("INCORRECT PASSWORD")
else:
    print("INCORRECT USER NAME")
