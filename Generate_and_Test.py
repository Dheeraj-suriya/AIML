count = 0

for pin in range(10000):
    pin = str(pin).zfill(4)

    d1 = int(pin[0])
    d2 = int(pin[1])
    d3 = int(pin[2])
    d4 = int(pin[3])

    if (d1 % 2 == 0 and d2 % 2 == 0 and
        d3 % 2 == 0 and d4 % 2 == 0):

        if d1 + d2 + d3 + d4 == 16:
            print(pin)
            count += 1

print("Total Valid PINs:", count)
