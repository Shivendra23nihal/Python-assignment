import math 
p = float(input('Enter the length of first side p: '))  
q = float(input('Enter the length of second side q: '))  
r = float(input('Enter the length of final side r: '))  

# calculate the semi-perimeter  
s = (p + q + r)/2

# calculate the area  
area = math.sqrt (s*(s-p)*(s-q)*(s-r))  
print('The area of the triangle is: ' , area)

