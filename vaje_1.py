''' Vaja 1
i = 0
vsota = 0
while i < 5:
    vsota = vsota + int(input('Vnesi ceno:'))
    i += 1
print('Vsota:', vsota)
'''

''' Vaja 2
st = int(input('Število izdelkov:'))
i = 0
vsota = 0
while i < st:
    vsota = vsota + int(input('Vnesi ceno:'))
    i += 1
print('Vsota:', vsota)
'''

''' Vaja 3
vsota = 0
while True:
    vnos = int(input('Vnesi ceno:'))
    vsota = vsota + vnos
    if vnos == 0:
        break
print('Vsota:', vsota)
'''

''' Vaja 4
i = 0
vsota = 0
while True:
    vnos = int(input('Vnesi ceno:'))
    vsota = vsota + vnos
    if vnos == 0:
        break
    i += 1
povp = vsota / i
print('Vsota:', vsota)
print('Povprečna cena:', povp)
'''

''' Vaja 5
stanje = 0
while True:
    sprememba = int(input('Sprememba: '))
    stanje += sprememba
    print('Stanje: ', stanje)
    if stanje < -100:
        break
print('Bankrot')
'''

''' Vaja 6
vsota = 0
i = 0
while i != 10 and vsota <= 100:
    cena = int(input('Cena: '))
    if cena == 0:
        break
    vsota = vsota + cena
    i += 1
print('Porabili boste ', vsota, ' za ', i, 'stvari')
'''

''' Vaja 7
import math
a = int(input('Vnesi a:'))
b = int(input('Vnesi b:'))
c = int(input('Vnesi c:'))

dis = (b ** 2) - (4 * a * c)

if dis < 0:
    print('Enačba nima realnih števil')

elif dis == 0:
    dis = (b * (-1) + math.sqrt(dis)) / 2 * a
    print('Enačba ima eno realno število:', dis)

elif dis > 0:
    dis_poz = (b * (-1) + math.sqrt(dis)) / 2 * a
    dis_neg = (b * (-1) - math.sqrt(dis)) / 2 * a
    print('Enačba ima dve realni števili:', dis_neg, 'in', dis_poz)
'''

''' Vaja 8
i = 1
while i <= 100:
    if i % 7 == 0:
        print('Bum')
    elif '7' in str(i):
        print('Bum')
    else:
        print(i)
    i += 1
'''

''' Vaja 9
n = int(input('Vnesi številko:'))
i = 1
vsota = 0
while i <= n:
    vsota = vsota + i
    i += 1
print(vsota)
'''

''' Vaja 10
import math

st = int(input('Vnesi število:'))
sqrt = math.isqrt(st) ** 2

if st == sqrt:
    print('Število je kvadrat')
else:
    print('Število ni kvadrat')
'''

''' Vaja 11
import math
st = int(input('Vnesi število kock:'))
i = 1
while True:
    if (i ** 2) >= st:
        print('Potrebujemo štatlo širine', i, 'v kateri je prostora še za ', (i ** 2) - st, 'kock')
        break
    i += 1
'''

''' Vaja 12 
st = int(input('Vnesi število:'))
i = 1
while i <= 18:
    if st % i == 0:
        print(i)
    i += 1
'''