allatok = ['maci', 'kacsa', 'pingvin', 'kígyó']

print('lista 1-es indexű (tehát 2.) eleme:')
print(allatok[1])
print('lista összes eleme egyesével: ')
for puluss in allatok:
    print(puluss)

print('listához elem hozzáadása: ')
uj_pluss = input('mit akarsz hozzáadni? ')

allatok.append(uj_pluss)

print('lista összes eleme: ')
print(allatok)

print(f'a lista hossza: {len(allatok)}')

print(f'a lista utolsó elemének indexe: {len(allatok) - 1}')

ures_lista = []

# ha még üres, akkor ez hibát dob:
# print(ures_lista[0])

allatok[2] = 'gorilla'
print(allatok)