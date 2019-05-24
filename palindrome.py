def IsPalindrome(num):
    numChars = list(num)  # Se divide el número en una lista de caracteres
    for i in range(0, int(len(numChars)/2)):
        if numChars[i] != numChars[len(numChars) - i - 1]:
            return False
    return True


def IsEven(num):
    value = int(num)
    if value % 2 == 0:
        return True
    return False


def IsPrime(num):
    value = int(num)
    if value == 2:
        return True
    for i in range(2, int((value/2)+1)):
        if value % i == 0:
            return False

    return True


def GetNumber():
    print("Introduzca un número entre 1 y 1000000:")
    num = input()
    aux = int(num)

    if IsEven(aux) and aux != 2:
        aux += 1

    while True:
        if aux % 2 != 0 or aux == 2:
            if IsPalindrome(str(aux)):
                if IsPrime(str(aux)):
                    print("La respuesta es: " + str(aux))
                    break
        aux += 2


def Main():
    GetNumber()


Main()
