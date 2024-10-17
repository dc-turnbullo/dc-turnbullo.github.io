mystring = str(input("enter a word to see if it is a pallendrome: "))
list1 = []
list2 = []
s = []
numchars = len(mystring)
print("there are characters:",numchars)
list1 = list(mystring)
print("list1 =",list1)
s = list1
print("s =",s)
print("list1 = ",list1)
for i in range(0,numchars):
    list2.append(s.pop())
print("finallist1 =",list1)

print("list2 = ",list2)
print("list1 =",list1)
if list2 == list1:
    print("pallendrome")
else:
    print("not pallendrome")