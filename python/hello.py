arr=[]
for i in range(0,6):
    a=input("enter no")  
    arr.append(a)
    print(arr)

low=0
high=len(arr)-1
mid=(low+high)//2

if(high%2==0):
    print(arr[mid])
else:
    print(arr[mid+1])