lst = [] #empty list
n = int(input("Enter the number of elements to be on the list:"))
for i in range(0,n):
    ele = int(input())
    lst.append(ele)
print("the list is :",lst)
# input taken
# now counting +ve numbers
positive_count=0
for num in lst:
    if num>0:
        positive_count+=1
print("the number of +ve numbers are:",positive_count)
