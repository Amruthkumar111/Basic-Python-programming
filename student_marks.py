#student marks
external_marks=int(input("enter the external marks"))
internal_marks=int(input("enter the internal marks"))
total_marks=external_marks+internal_marks
if total_marks>35:
  print("pass")
else:
  print("fail")
