mystring = str(input("Enter a word to see if it is a palindrome: "))
list1 = list(mystring)
list2 = []

numchars = len(mystring)
print("There are characters:", numchars)
print("list1 =", list1)

s = list1.copy()
print("s =", s)

for i in range(numchars):
    list2.append(s.pop())

print("final list1 =", list1)
print("list2 =", list2)
print("list1 =", list1)

if list2 == list1:
    print("Palindrome")
else:
    print("Not a palindrome")