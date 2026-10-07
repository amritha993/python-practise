username = input("Enter your username:")


if username == "admin":
    password = input("Enter your password:")

    if password =="python123":
       OTP = input("OTP verified(Yes/No):") == "Yes"

       if OTP == True:
         print("Login Successful")
       else:
         print("OTP Required")
    else:
       print("Wrong Password")
else:
   print("Invalid User")