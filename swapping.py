x = input('Enter value of x: ')
y = input('Enter value of y: ')
temp = x
x = y
y = temp
print('The value of x after swapping: {}'.format(x))
print('The value of y after swapping: {}'.format(y))
print("-----------------------------------------------------------------------")
print("without temp")

x = 5
y = 10
x, y = y, x
print("x =", x)
print("y =", y)