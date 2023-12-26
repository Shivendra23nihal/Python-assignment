number= []
num=int(input('How many numbers:'))
for n in range (num):
    x=int (input('Enter number'))
    number.append(x)
    print("Sum of numbers in the given list is :",sum(number))