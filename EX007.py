import random
INICIO = 0
par = 0
somaimpar = 0
lista = []
while( INICIO < 255):
     INICIO += 1
     aux = int(random.randint(1,100))
     lista.append(aux)
     if (aux % 2 == 1):
       somaimpar += aux
print(f"A média da lista é: {sum(lista) / len(lista): .2f} ")
print(f'o maior numero: {max(lista)}')
print(f'o menor numero: {min(lista)}')
print(f'A soma dos numeros impares é: {somaimpar} ')