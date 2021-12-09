print('1. megoldás: ')
for x in range(1, 100, 2):
    print(x, end=' ')

print('\n\n2. megoldás: ')
for x in range(100):
    if x % 2 == 1: print(x, end=' ')
    if x % 10 == 0: print()

print('\n\n3. megoldás')
x = 1
for i in range(50):
    print(x, end=' ')
    x += 2