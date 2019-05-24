def GetMaxCommon(str1, str2):
    cant1 = len(str1)
    maximum = 0
    answer = ""

    for i in range(cant1):
        for j in range(cant1):
            if j < (cant1 - i):
                temp = str1[i:(cant1-j)]
                if temp in str2 and len(temp) > maximum:
                    answer = temp
                    maximum = len(temp)
    print(answer)


def GetInput():
    print("Digite la primera cadena de ADN:")
    first_dna = input()
    print("Digite la segunda cadena de ADN:")
    second_dna = input()
    GetMaxCommon(first_dna, second_dna)


def Main():
    GetInput()


Main()
