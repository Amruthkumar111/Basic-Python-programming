#temperature
Temp=float(input("Enter TEMPERATURE: "))
if Temp==37:
  print("NORMAL")
elif Temp<37:
  print("COLD")
elif Temp>37:
  print("FEVER")
else:
  print("Invalid Temperature")
