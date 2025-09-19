# linear search
def linear_search(arr,target):
    for i in range(len(arr)):
        if arr[i]==target:
            return i
    return -1
arr=list(map(int,input("ENTER ELEMENTS: ").split()))
target=int(input("ENTER A VALUE: "))
result=linear_search(arr,target)
if result != -1:
    print("Element found")
else:
    print("Element not found")
