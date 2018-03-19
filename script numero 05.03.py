numeros = [5,2,16,7,8,9,20,24]

maior= numeros[0]
menor= numeros[0]
contador=0
total=0
for n in numeros:
    if n > maior:
        maior = n
    if n < maior:
        menor = n
    total= total+ n
    contador = contador +1

media = total/contador

print('o maior elemento: %d' %(maior))
print('o menor elemento: %d' %(menor))
print ('a média: %d' %(media))
