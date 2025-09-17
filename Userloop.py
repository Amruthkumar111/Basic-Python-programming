# user and password with loop
a="ak"
b="111"
while True:
    user = input("Enter user name: ")
    if user==a:
        password = input("Enter password: ")
        if password==b:
            print("WELCOME")
            break
        else:
            print("INCORRECT PASSWORD")
    else:
        print("INCORRECT USER NAME")
