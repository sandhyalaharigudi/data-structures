def insertion_sort(lst):
    for i in range(1,len(lst)):
        x=lst[i]
        j=i-1
        while j>0 and x<list[j]:
            lst[j+1]=lst[j]
            j=j-1
            lst[j+1]=x
        return lst
n=int(input("enter no of elements:"))
l=[]
for i in range(n):
    ele=int(input("enter element:"))
    l.append(ele)
print(insertion_sort(l)) 