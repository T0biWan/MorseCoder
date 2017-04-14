from morsecode import morsecode


def convertStringToMorsecode(string):
    code = ""
    for char in string.lower():
        if char in morsecode:
            code += morsecode[char] + " "
        else:
            code += "X "

    return code[0:-1]

def convertMorseCodeToString(code):
    string = ""
    morsecodeKeysAndValuesInverted = dict(zip(morsecode.values(), morsecode.keys()))

    for letter in code.split(" "):
        if letter in morsecodeKeysAndValuesInverted:
            string += morsecodeKeysAndValuesInverted[letter]
        else:
            string += "X"

    return string


print(convertStringToMorsecode("Fries Over Guys"))
print(convertMorseCodeToString("..-. .-. .. . ... 	 --- ...- . .-. 	 --. ..- -.-- ..."))
