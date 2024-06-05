import math

def addOneBit(final, num):

    i = final[len(final) - 1]
    if(i == "0"):
        newfinal = ""

        for j in range(len(final) - 1, 0,-1): 
            newfinal += final[j]
        newfinal += "1"
    else:
        count = 1;
        j = len(final) - 2
        while i != "0":
            j -= 1
            count += 1
            i = final[j]
            
    final = newfinal
    print(final)


num = int(input("Enter a number "))
bit = int(input("Enter bit amount "))

while (2 ** (bit - 1)) - 1 < num:

    print(f"The number is too big for your bit amount, you need at least {math.ceil(math.log2(num + 1)) + 1} bits ")
    print("1. change number ")
    x = int(input("2. complete bit amount "))

    while x != 1 and x != 2:
        x = input("entered wrong answer, please enter 1 or 2 ")

    match x:
        case 1: num = int(input("Enter a number "))
        case 2: bit = math.ceil(math.log2(num + 1)) + 1

final = ""
for i in range(bit):
    final += "0"

addOneBit(final, num)
