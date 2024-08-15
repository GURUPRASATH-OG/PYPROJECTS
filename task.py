a=int(input('enter a number: '))
b=int(input('enter b number: '))
print(f'a before swapping {a}, b before swapping {b}')
a=a+b
b=a-b
a=a-b
print(f'a after swapping {a}, b after swapping {b}')