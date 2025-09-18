#hotel management
print("Are You an Existing Customer (True or False): ")
a=bool(input())
if True:
  print("Welcome Back: ")
else:
  print("Please Register")
print("welcome to hotel", "\n1.Tiffins ","\n2.Meals","\n3.Juices","\n4.Snacks")
choice=int(input("Enter your choice: "))
if choice==1:
  print("Tiffins: ","\n1.Idly","\n2.Dosa","\n3.Poori")
elif choice==2:
  print("Meals: ","\n1.Biryani","\n2.Veg-Biryani","\n3.Meals")
elif choice==3:
  print("Juices: ","\n1.Mango","\n2.Soft","\n3.Orange")
elif choice==4:
  print("Snacks: ","\n1.Samosa","\n2.Bajji/Bonda","\n3.Cakes")
else:
  print("Invalid Choice")
subchoice=int(input("Enter your choice: "))
if choice==1 and subchoice==1:
  print("Idly: 30 Rupees")
  x=int(input("Enter the quantity: "))
  print("Total Amount: ",x*30)
elif choice==1 and subchoice==2:
  print("Dosa: 50 Rupees")
  x=int(input("Enter the quantity: "))
  print("Total Amount: ",x*50)
elif choice==1 and subchoice==3:
  print("Poori: 40 Rupees")
  x=int(input("Enter the quantity: "))
  print("Total Amount: ",x*40)
elif choice==2 and subchoice==1:
  print("Biryani: 150 Rupees")
  x=int(input("Enter the quantity: "))
  print("Total Amount: ",x*150)
elif choice==2 and subchoice==2:
  print("Veg-Biryani: 120 Rupees")
  x=int(input("Enter the quantity: "))
  print("Total Amount: ",x*120)
elif choice==2 and subchoice==3:
  print("Meals: 100 Rupees")
  x=int(input("Enter the quantity: "))
  print("Total Amount: ",x*100)
elif choice==3 and subchoice==1:
  print("Mango: 30 Rupees")
  x=int(input("Enter the quantity: "))
  print("Total Amount: ",x*30)
elif choice==3 and subchoice==2:
  print("Soft: 20 Rupees")
  x=int(input("Enter the quantity: "))
  print("Total Amount: ",x*20)
elif choice==3 and subchoice==3:
  print("Orange: 40 Rupees")
  x=int(input("Enter the quantity: "))
  print("Total Amount: ",x*40)
else:
  print("Invalid Choice")
