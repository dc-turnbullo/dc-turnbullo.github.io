numbers = []
average = 0
total = 0
for i in range(0,6):
    num = int(input("Enter number"))
    numbers.append(num)
#next i
count = 5
while count >= 0:
    print(numbers[count])
    total = total + numbers[count]
    count -=1
#next i
print(total)
print(total/6)
