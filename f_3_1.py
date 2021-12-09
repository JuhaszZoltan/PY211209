nevek = ['Dávid', 'Imola', 'Viki', 'Gajdi', 'Dávid']
magassagok = []

for nev in nevek:
    m = int(input(f'{nev} magassága: '))
    magassagok.append(m)

for i in range(len(nevek)):
    print(f'{nevek[i]}: {magassagok[i]} cm magas')

sum = 0
for m in magassagok:
    sum += m

print(f'átlagmagasság: {sum / len(magassagok)} cm')

maxi = 0

for i in range(1, len(magassagok)):
    if magassagok[i] > magassagok[maxi]:
        maxi = i

print(f'a legmagasabb {magassagok[maxi]} cm, azaz {nevek[maxi]}')

nevek.sort()

print(nevek)