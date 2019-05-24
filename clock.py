def CalculateLeds(segs):
    leds = 0
    temp = 0
    digits = {
        0: 6,
        1: 2,
        2: 5,
        3: 5,
        4: 4,
        5: 5,
        6: 6,
        7: 3,
        8: 7,
        9: 6
    }
    clock = [0, 0, 0, 0, 0, 0]

    while True:
        if clock[5] == 10:
            clock[4] += 1
            clock[5] = 0

        if clock[4] == 6:
            clock[3] += 1
            clock[4] = 0

        if clock[3] == 10:
            clock[2] += 1
            clock[3] = 0

        if clock[2] == 6:
            clock[1] += 1
            clock[2] = 0

        if clock[1] == 10:
            clock[0] += 1
            clock[1] = 0

        if clock[0] == 2 and clock[1] == 4:
            for i in range(0, 6):
                clock[i] = 0

        for i in range(0, 6):
            leds += digits[clock[i]]

        clock[5] += 1
        temp += 1

        if temp > segs:
            break

    print(leds)


def GetInput():
    segs = int(input())
    CalculateLeds(segs)


def Main():
    GetInput()


Main()
