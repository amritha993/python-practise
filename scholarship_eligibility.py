marks = int(input("Enter your marks:"))
if marks< 75 :
  print("Not Eligible")

elif marks>=90:
  print("Scholarship Approved")
elif marks>=75 :
    sports = input("Do you have Sports Quota(Yes/No):")=="Yes"
    if sports:
      print("Scholarship Approved")
    else:
      print("Rejected")