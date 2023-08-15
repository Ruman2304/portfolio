def binarysearch(list, key):
    low = 0
    high = len(list) - 1
    mid = 0

    while low <= high:
        mid = (high + low) // 2


        if list[mid] < key:
            low = mid + 1

        elif list[mid] > key:
            high = mid - 1


        else:
            return mid

            # element was not present in the list, return -1
    return -1







list=[1,2,3,4,5,6,7,8]
key=5

result=binarysearch(list,key)

if result!=-1:
    print(" found at",result)
else:
    print("found not")




