a2 = int(input('enter a2 '))
a1 = int(input('enter a1 '))
b = int(input('enter b '))

c2 = a2 + (a1+b)//10
c1 = (a1+b)%10

print("числа полученного значения: {0}, {1}".format(c2, c1))