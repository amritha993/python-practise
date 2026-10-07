username = input("Enter username:")


if username == "student":
    password = input("Enter your password:")
   
    if password == "python":
        fa = input("Do you have 2FA verification(Yes/No)")=="Yes"
        if fa ==True:
          print("Login Successful")
        else:
           print("2FA certificate Required")
    else:
       print("Invalid Password")
else:
   print("Invalid User")       