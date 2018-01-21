# Justin Edwards
# Lab 2 Binary Decimal Conversion
# CS 2705 Fundamentals of Networking


def decimalToBinary(oct1, oct2, oct3, oct4):
    binOct1 = bin(oct1)[2:].zfill(8)
    binOct2 = bin(oct2)[2:].zfill(8)
    binOct3 = bin(oct3)[2:].zfill(8)
    binOct4 = bin(oct4)[2:].zfill(8)

    decimalIP = "{0}.{1}.{2}.{3}"
    binaryIP = "The binary IP address for " + decimalIP.format(oct1, oct2, oct3, oct4) + " is {0}.{1}.{2}.{3}"
    print(binaryIP.format(binOct1, binOct2, binOct3, binOct4))


def binaryToDecimal(oct1, oct2, oct3, oct4) :
    decOct1 = int(oct1, 2)
    decOct2 = int(oct2, 2)
    decOct3 = int(oct3, 2)
    decOct4 = int(oct4, 2)

    binaryIP = "{0}.{1}.{2}.{3}"
    decimalIP = "The decimal IP address for " + binaryIP.format(oct1, oct2, oct3, oct4) + " is {0}.{1}.{2}.{3}"
    print(decimalIP.format(decOct1, decOct2, decOct3, decOct4))

print("Decimal to Binary:")
decimalToBinary(192, 168, 16, 13)
decimalToBinary(164, 10, 241, 2)
decimalToBinary(10, 244, 116, 15)
decimalToBinary(15, 255, 200, 153)
decimalToBinary(172, 99, 62, 9)

print("\nBinary to Decimal:")
binaryToDecimal('10110100', '11101011', '00001000', '10010001')
binaryToDecimal('10001100', '11111111', '11000000', '00000001')
binaryToDecimal('00010001', '11001100', '00000001', '00010010')
binaryToDecimal('11100111', '00110011', '10101010', '11111110')
binaryToDecimal('00010111', '11101110', '01010101', '10000000')
