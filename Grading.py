# to check grade using marks
a=int(input("Enter the marks"))
if a<=100 and a>=91:
  print("Ex")
  print("Excellent")
elif a<=90 and a>=81:
  print("A")
  print("Good")
elif a<=80 and a>=71:
  print("B")
  print("OK")
elif a<=70 and a>=61:
  print("C")
  print("Need Improvement")
elif a<=60 and a>=51:
  print("D")
  print("Workhard")
elif a<=50 and a>=41:
  print("P")
elif a<=40 and a>=0:
  print("F")
else:
  print("Enter the valid marks")
