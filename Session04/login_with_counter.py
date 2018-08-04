print("Hi there,this is a super gateway")

username = input("Username: ")

loop =True
count = 0

while loop:
    if username == "c4e":
        password = input("Password :")
        if password == "codethechange":
            print("Welcome, ", username)
            break
        else:
            print("Password is incorrect")

    else:
        print("Password is incorrect")

    count += 1
    if count == 3:
        print("Your failed to login 3 times ,go away")
        loop =False

