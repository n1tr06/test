import math

def toBinList(num, bit):
    binList = [0] * bit
    for i in range(bit-1, -1, -1):
        binList[i] = num % 2
        num = num // 2
    return binList

def addOneBit(list):

    for i in range(len(list)-1, -1 , -1):
        if i == 0:
            break;
        
        elif list[i] == 0:
            list[i] = 1
            break;
        
        else:
            list[i] = 0

    return list
            
def reverseBit(list):

    for i in range(0, len(list)):
        if list[i] == 0:
            list[i] = 1

        else:
            list[i] = 0

    return list

def listToString(list):
    result = ""
    for i in range(len(list)):
        result += str(list[i])
    return result


num = int(input("Enter a number: "))
bit = int(input("Enter bit amount: "))

while (2 ** (bit - 2)) - 1 < num:

    print(f"The number is too big for your bit amount, you need at least {math.ceil(math.log2(num + 1)) + 2} bits.")
    print("1. Change number")
    print("2. Change bit amount")
    print(f"3. Complete bit amount ({math.ceil(math.log2(num + 1)) + 2})")
    x = input("Enter 1, 2 or 3: ")

    while x not in [1, 2, 3]:
        x = input("Entered wrong answer, please enter 1, 2 or 3: ")

    match x:
        case 1: num = int(input("Enter a number: "))
        case 2: bit = int(input("Enter bit amount: "))
        case 3: bit = math.ceil(math.log2(num + 1)) + 2

final = toBinList(num, bit)

final = reverseBit(final)
addOneBit(final)

if num == 0:
    final[0] = 0

print(listToString(final))