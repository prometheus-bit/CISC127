#Name: Thomas Hunter
#Date: September 6, 2017
#This program prints: String from STDIN in ascii to STDOUT

print("Enter a phrase: ", end='')
print("In ASCII:", *(input().encode()), sep="\n")
