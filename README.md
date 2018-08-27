# MagicMissile
This is a script to automate the decoding of various encoding types.

The intended use case is to call the script, select the desired input type
(base64, hex, decimal, or binary), paste the input encoded string, which will
then, hopefully, decode correctly.

Current version 1.0
--------------------
___  ___            _       ___  ____         _ _      
|  \/  |           (_)      |  \/  (_)       (_) |     
| .  . | __ _  __ _ _  ___  | .  . |_ ___ ___ _| | ___ 
| |\/| |/ _` |/ _` | |/ __| | |\/| | / __/ __| | |/ _ \
| |  | | (_| | (_| | | (__  | |  | | \__ \__ \ | |  __/
\_|  |_/\__,_|\__, |_|\___| \_|  |_/_|___/___/_|_|\___|
               __/ |                                   
              |___/                                    

It works, most of the time, and it's not really very pretty.

It's written in Python 3.27, so if you try to launch it in python2
it'll die and not work, so call it with python3.

When prompted to make a selection, use the character letter of your
choice, either A, B, C, or D, it's case insensitive. If you enter
an option it wasn't expecting, it'll spit out an error message
and you'll have to call the script again.
