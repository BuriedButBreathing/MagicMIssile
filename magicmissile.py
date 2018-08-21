# Add in decoding modules!!
# Comment things!!
#Library imports
import base64
import codecs
#Decode type select
print('Select which encoding the input string is in: \nA: Base64\nB: Hex\nC: Decimal\nD: Binary')
selection = str(input())
print('Your selection was: ' + (selection))
#Base64 Decoding
if selection in ['a', 'A']:
    b64string = str(input('Paste Base64 string to be decoded: '))
    b64string = b64string + '================='
    decodedb64 = base64.b64decode(b64string).decode('ascii')
    print(decodedb64)
# Hex Decoding
elif selection in ['B', 'b']:
    hexstring = str(input('Paste Hex string to be decoded: '))
    decodedhex = codecs.decode(hexstring, "hex").decode('utf-8')
    print(decodedhex)
# Decimal Decoding
elif selection in ['C', 'c']:
    print('Paste decimal string to be decoded')
    decstring = input().split()
    decoutput = []
    for x in decstring:
        print(x)
        decstringint = int(x)
        decoutput.append(chr(decstringint))
    print("".join(decoutput))
# Binary decoding
elif selection in ['D', 'd']:
    print("Binary")
    print('Paste Binary string to be decoded: ')
    bininput =input().split()
    binoutput = []
    for x in bininput:
        character = chr(int(x,2))
        binoutput.append(character)
    final_string = "".join(binoutput)
    print(final_string)
else:
    print("Choose again, but choose correctly this time")
