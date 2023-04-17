INICIO = 0
FINAL = 100
contN = 0
contP = 0
LISTA = []
LISTA_PAR = []
LISTA_IMP = []
while (INICIO <= 100):
    LISTA.append(INICIO)
    if (INICIO % 2 == 0):
        LISTA_PAR.append(INICIO)
        contP += 1
    elif (INICIO % 2 == 1):
        LISTA_IMP.append(INICIO)
        contN += 1

    INICIO += 1
print(LISTA_PAR)
print(LISTA_IMP)