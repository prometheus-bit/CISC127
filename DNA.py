#Name: Matthew Prussman
#Date: September 1, 2017
#This program prints: The GCpercent of a DNA sequence to STDOUT
"""
    This program reads from STDINPUT a DNA Sequence of the form [ACGT]+ and computes the GC Percent

    The user is prompted to enter a DNA Sequence following:

        >>>Enter DNA Sequence:

    Input can either be from the keyboard or by redirection from a pipe or file.
    Input is expected to be of the form of the regular expression [ACGT]+. Such a string would be...

    Example:
        ACGGGGCTAGCTAGCTTTACGAACTCG

    If a valid sequence is given as input, execution continues to then compute the percent
    of the sequence that is comprised of GC nucleotides.  The result is printed to STDOUT.

    In the case of invalid input, the points of error in the DNA sequence given as input will be
    documented and printed to STDOUT.

"""

import re
import sys
import traceback

print("Enter DNA Sequence: ")
try:
    DNA = input().upper()
    validDNA = re.fullmatch("[ACGT]+", DNA)
    if validDNA:
        numC = DNA.count('C')
        numG = DNA.count('G')
        gc = (numC + numG) / len(DNA)
        gcPercent = gc * 100
        print(gcPercent)
    else:
        invalid = []
        for Nuc in re.finditer("[^ACGT]+", DNA):
            invalid.append('%02d - %02d: %s' % (Nuc.start(), Nuc.end(),
                           Nuc.group(0)))
        raise ValueError(invalid)
except EOFError as err:
    exc_type, exc_value, exc_traceback = sys.exc_info()
    traceback.print_exception(exc_type, exc_value, exc_traceback,
                              limit=2, file=sys.stdout)
    print("Possible Cause: EOF key or Empty File")
except ValueError as err2:
    print("Invalid DNA Sequence: Errors in Sequence at\n[Start-End: Sequence]")
    for err in err2.args[0]:
        print(err)
