# Se capturan los nombres, se separan y se colocan en una lista.
def GetList():
    inputList = input()
    returnList = inputList.split(' ')
    return returnList

# Se capturan las opciones del usuario. Si se usa el 0 al principio, se termina el programa
# y se imprime la salida. Si se usa el 1, se continúa con la captura de los nombres de la dinastía.
#
# Para el caso de los sucesores, se utiliza el 1 para proceder con la captura de sus nombres.


def GetInput(DynastiesDict, SuccessorsDict):
    i = 0
    while True:
        print("0 -> Terminar. 1 -> Proceder")
        cant = input()
        if cant == '0':
            break
        DynastiesDict[i] = GetList()
        while True:
            print("1 -> Proceder")
            cant = input()
            if cant == '1':
                break
        SuccessorsDict[i] = GetList()
        i += 1

    print("")

# Función que se encarga de contar los miembros de la dinastía para asignar un número a los sucesores.


def CountKings(DynastiesDict, SuccessorsDict):
    for i in range(len(DynastiesDict)):
        newDynastyDict = {}
        newSuccessorsDict = {}

        for name in DynastiesDict[i]:
            if name in newDynastyDict:
                newDynastyDict[name] += 1
            else:
                newDynastyDict[name] = 1
        for name in SuccessorsDict[i]:
            newSuccessorsDict[name] = 1
        for name in SuccessorsDict[i]:
            if name in newDynastyDict:
                newDynastyDict[name] += 1
                print(name + " " + str(newDynastyDict[name]))
            else:
                if name in newSuccessorsDict:
                    print(name + " " + str(newSuccessorsDict[name]))
                    newSuccessorsDict[name] += 1
        print("")


def Main():
    DynastiesDict = {}
    SuccessorsDict = {}
    GetInput(DynastiesDict, SuccessorsDict)
    CountKings(DynastiesDict, SuccessorsDict)


Main()
