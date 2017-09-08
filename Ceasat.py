# Name: Matthew Prussman
# Date: September 1, 2017
# This program prints: ASCII code of characters from STDIN to STDOUT

import sys

def byteReadLine():

    try:
        return sys.stdin.buffer.readline()
    except:
        print("read error")



def bitLessOne(bit):

    shifter = 1
    bit ^= shifter

    while bit > bit ^ shifter:
        shifter <<= 1
        bit ^= shifter

    return bit

def cipherBytes(bytePhrase):

    if bytePhrase == 97:
        yield 122
    else:
        yield bitLessOne(bytePhrase)

def prettyPrintCipher(gen):

    for byte in gen:
        for ciphered in cipherBytes(byte):
            yield f'{ciphered:c}'

if __name__ == '__main__':
    print("Please enter phrase")
    print("Your word in code is:\n", *prettyPrintCipher(byteReadLine()), sep='')
