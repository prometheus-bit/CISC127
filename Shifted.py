# Name: Matthew Prussman
# Date: September 1, 2017
# This program prints: ASCII code of characters from STDIN to STDOUT

print("Enter a word:", end="")
conversion_fmt = lambda x: f'{(x - 1 if (x % 122) else 97):c}'
print("Your word in code is:\n", *(conversion_fmt(_) for _ in input().encode()), sep='')
