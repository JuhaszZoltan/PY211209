n = int(input('szám: '))
prim = True
if n < 1: print('figyu, ez nem így működik tesó -.-')
else:
    print(f'{n} osztói:', end=' ')
    print(f'{1}', end=' ')
    for i in range(2, n // 2 + 1):
        if n % i == 0:
            print(i, end = ' ')
            prim = False
    if n == 1:
        print()
        prim = False
    else: print(f'{n}')
    if prim: print(f'{n} prímszám')
    else: print(f'{n} nem prímszám')