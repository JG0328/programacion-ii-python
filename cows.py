def bubbleSort(arr, arr2, arr3):
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
                arr2[j], arr2[j+1] = arr2[j+1], arr2[j]
                arr3[j], arr3[j+1] = arr3[j+1], arr3[j]
    

print("Digite el total de vacas que estan a la venta")
cant = int(input())

print("Digite el peso total que puede cargar el camion")
maxWeight = int(input())

print("Digite el peso de cada vaca separado por un espacio")
cowsWeight = input()
cowsWeight = cowsWeight.split(" ")

print("Digite la cantidad(en litros) de leche que produce cada vaca separada por un espacio")
cowsMilk = input()
cowsMilk = cowsMilk.split(" ")


distribution = {}


for i in range(0, len(cowsWeight)):
    distribution[i] = float(cowsMilk[i])/float(cowsWeight[i])

selectedCows = []
selectedCows.append([])

bubbleSort(distribution, cowsWeight, cowsMilk)

travelWeight = 0
travelLiters = 0


for i in range(len(distribution)):
    if (travelWeight + int(cowsWeight[i])) <= maxWeight:
        travelWeight = travelWeight + int(cowsWeight[i])
        travelLiters = travelLiters + int(cowsMilk[i])


print(str(travelLiters))
