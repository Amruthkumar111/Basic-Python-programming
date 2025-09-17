#sum of cubes
m=int(input("Enter m value: "))
n=int(input("Enter n value: "))
if m>n:
    print(0)
else:
    s=0
    for i in range(m,n+1):
        s += i**3
    print(s)
