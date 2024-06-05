import math

def addOneBit(arr):

    for i in range(len(arr)-1, -1 , -1):
        if i == 0:
            break;
        
        elif arr[i] == 0:
            arr[i] = 1
            break;
        
        else:
            arr[i] = 0

    return arr
            
def reverseBit(arr):

    for i in range(0, len(arr)):
        if arr[i] == 0:
            arr[i] = 1

        else:
            arr[i] = 0

    return arr



num = int(input("Enter a number "))
bit = int(input("Enter bit amount "))

while (2 ** (bit - 1)) - 1 < num:

    print(f"The number is too big for your bit amount, you need at least {math.ceil(math.log2(num + 1)) + 1} bits ")
    print("1. change number ")
    x = int(input("2. complete bit amount \n"))

    while x != 1 and x != 2:
        x = input("entered wrong answer, please enter 1 or 2 ")

    match x:
        case 1: num = int(input("Enter a number "))
        case 2: bit = math.ceil(math.log2(num + 1)) + 1

final = [0] * bit

for i in range(0, num):
    final = addOneBit(final)

final = reverseBit(final)
print(addOneBit(final))


