#calculator
a=int(input("Enter a value"))
b=int(input("Enter b value"))
c=int(input("Enter your choice : "))
if c==1:
  print("The SUM is:",a+b)
elif c==2:
  print("The difference is: ",a-b)
elif c==3:
  print("The product is: ",a*b)
elif c==4:
  print("The Division is: ",a/b)
else:
  print("Invalid choice")
