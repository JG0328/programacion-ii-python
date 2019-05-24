# Diccionario con cada letra y su valor correspondiente
letters = {
    "A":2,
    "B":22,
    "C":222,
    "D":3,
    "E":33,
    "F":333,
    "G":4,
    "H":44,
    "I":444,
    "J":5,
    "K":55,
    "L":555,
    "M":6,
    "N":66,
    "O":666,
    "P":7,
    "Q":77,
    "R":777,
    "S":7777,
    "T":8,
    "U":88,
    "V":888,
    "W":9,
    "X":99,
    "Y":999,
    "Z":9999,
    " ":0
}

print("Digite una frase:")
phrase = input()
phrase = phrase.upper()
output = []

for i in phrase:
    output.append(str(letters[i]) + ' ')

# Formato de salida, se eliminan los corchetes y comas que salen al imprimir una lista
print(''.join(map(str, output)))