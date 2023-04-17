import random
lista = []
INICIO = 0
numeromaior = 0
contador = 0
while ( INICIO < 100):
    INICIO += 1
    aux = int(random.randint(1,100))
    if (aux > numeromaior):
       numeromaior = aux
       contador += 1
print (f"Quantidade {contador} ")
print (f"Maior numero {numeromaior} ")