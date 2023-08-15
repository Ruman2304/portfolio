def binarysearch(key,n,list):

    for i in range(0,n):
        if list[i]==key:
            return i;

    return -1

list=[1,2,3,4,5,6]
key=5
n=len(list)
index=binarysearch(key,n,list)

if index==-1:
    print("not found")
else:
    print("found at los ",index)


