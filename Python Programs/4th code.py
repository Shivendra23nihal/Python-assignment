count = int(input("Enter the total number you want to enter:"))
i=0
sum = 0
for i in range(count):
    x = int(input("Enter the number:"))
    sum = sum + x
avg = sum / count
print("The average is:", avg)