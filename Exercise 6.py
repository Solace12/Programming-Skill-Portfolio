CorrectPassword ="12345"
password = ""

while password != CorrectPassword:
    password = input("Enter Password: ")
    if password != CorrectPassword:
        print("Incorrect password Please try again!")
    else:
        print("The password you entered is Correct!")
