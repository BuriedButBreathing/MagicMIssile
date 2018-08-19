# Add in decoding modules!!
# Comment things!!

import base64
print('Select which encoding the input string is in: \nA: Base64\nB: Hex\nC: Decimal\nD: Binary')
selection = str(input())
print('Your selection was: ' + (selection))
if selection in ['a', 'A']:
    b64string = str(input('Paste Base64 string to be decoded: '))
    base64.b64decode(b64string)
    print(b64string)
elif selection in ['B', 'b']:
   print("Hex")
elif selection in ['C', 'c']:
    print("Decimal")
elif selection in ['D', 'd']:
    print("Binary")
else:
    print("Choose again, but choose correctly this time")
