def Binarysearch(l,low,high,key):
    while low<=high:
            mid=(low+high)//2
            if l[mid]==key:
                return mid
            elif l[mid]>key:
                high=mid-1
            else:
                low=mid+1
    return-1
l=[7,8,9,10,15,18]
low=0
n=len(l)-1
key=int(input("enter the key element:"))
result=Binarysearch(l,low,n,key)
if result==-1:
    print("element not found")
else:
    print("element not found at",result)