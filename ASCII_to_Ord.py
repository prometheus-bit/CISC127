# Name: Matthew Prussman
# Date: September 1, 2017
# This program prints: ASCII code of characters from STDIN to STDOUT
"""

"""
import sys
import traceback

print("Enter a phrase: ", end="")

try:
    for asciiCode in map(lambda x: ord(x), input()):
        print(asciiCode)
    print(ascii("12,27,89,76"))
except EOFError as eofError:
    exc_type, exc_value, exc_traceback = sys.exc_info()
    traceback.print_exception(exc_type, exc_value, exc_traceback,
                              limit=2, file=sys.stdout)
    print("EOF encountered: Please check data source")

