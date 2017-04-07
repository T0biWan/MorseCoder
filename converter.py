from morsecode import morsecode

def convertStringToMorsecode(string):
    code = ""
    for char in string.lower():
        if char in morsecode:
            code += morsecode[char] + " "
        else:
            code += "X "

    return code[1:-1]

print(convertStringToMorsecode("Du bist ja auch keine Flasche"))
