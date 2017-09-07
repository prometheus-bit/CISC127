# Name: Matthew Prussman
# Date: September 1, 2017
# This program prints: ASCII code of characters from STDIN to STDOUT

def cipher(bytes):

    try:
        conversion_fmt = lambda x: f'{(x - 1 if (x % 122) else 97):c}'
        for _ in bytes:
            yield conversion_fmt(_)
    except:
        print("Error")

print("Enter a word:", end="")
phrase = input().encode()
phrase = cipher(phrase)
print("Your word in code is:")
for char in phrase:
    print(char, sep='', end='')