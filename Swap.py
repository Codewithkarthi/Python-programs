#swapping of numbers without using third variable
x = 5

y = 7
 

print ("Before swapping: ")

print("Value of x : ", x, " and y : ", y)
 
# code to swap 'x' and 'y'

x, y = y, x
 

print ("After swapping: ")

print("Value of x : ", x, " and y : ", y)


#program to swap two numbers using third variable

#Input
num1 = input('Enter value of first number (num1): ')
num2 = input('Enter value of second number (num2): ')

# create a temporary variable and swap the values
temp = num1
num1 = num2
num2 = temp

#Output
print('The value of num1 after swapping: {}'.format(num1))
print('The value of num2 after swapping: {}'.format(num2))
