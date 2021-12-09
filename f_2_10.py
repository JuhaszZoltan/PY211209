print('\n\n')
for x in range(99, 0, -2):
    print(x, end=' ')
print('\n\n')
for x in range(1, 100):
    if (100 - x) % 2 == 1: print(100 - x, end=' ')
print('\n\n')
x = 99
for i in range(50):
    print(x, end=' ')
    x -= 2
print('\n\n')
x = 99
for i in range(50):
    print(x - 2* i, end=' ')