#to check age group
n=int(input("Enter the age"))
if n<=13 and n>1:
  print("Child")
elif n<=19 and n>=14:
  print("Teenage")
elif n>=20:
  print("Adult")
else:
  print("invalid age")
