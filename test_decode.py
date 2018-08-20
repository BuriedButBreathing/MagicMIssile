# Add in decoding modules!!
# Comment things!!

import base64
import codecs
print('Select which encoding the input string is in: \nA: Base64\nB: Hex\nC: Decimal\nD: Binary')
selection = str(input())
print('Your selection was: ' + (selection))
if selection in ['a', 'A']:
    b64string = str(input('Paste Base64 string to be decoded: '))
    decodedb64 = base64.b64decode(b64string)
    print(decodedb64)
elif selection in ['B', 'b']:
    hexstring = str(input('Paste Hex string to be decoded: '))
    decodedhex = codecs.decode(hexstring, "hex").decode('utf-8')
    print(decodedhex)
elif selection in ['C', 'c']:
    decstring = str(input('Paste decimal string to be decoded: '))
    decstringint = int(decstring)
    decodedec = chr(decstringint)
    print(decodedec)
elif selection in ['D', 'd']:
    print("Binary")
else:
    print("Choose again, but choose correctly this time")
