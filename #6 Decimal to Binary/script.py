number = int(input('Input a number between 1 and 255: '))

binary = [0, 0, 0, 0, 0, 0, 0, 0]

for i in range(len(binary)):
    power = len(binary) - 1 - i

    if number >= 2**power:
        binary[i] = 1
        number -= 2**power
    
    print(binary[i], end='')    
print()
