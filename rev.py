#rev.py
#art
print("|=================================================|")
print("|  _____             _____ _        _             |")
print("| |  __ \           / ____| |      (_)            |")
print("| | |__) |_____   _| (___ | |_ _ __ _ _ __   __ _ |")
print("| |  _  // _ \ \ / /\___ \| __| '__| | '_ \ / _` ||")
print("| | | \ \  __/\ V / ____) | |_| |  | | | | | (_| ||")
print("| |_|  \_\___| \_/ |_____/ \__|_|  |_|_| |_|\__, ||")
print("|                                            __/ ||")
print("|    By P4nduhz                             |___/ |")
print("|    github.com/PPanduhz                          |")
print("|=================================================|")
print()
import argparse

#create an ArgumentParser object
parser = argparse.ArgumentParser(description = 'Reverse a String')
#declare arguments
parser.add_argument('-s', type = int, required = False, help='removes spaces from the reversed string')
parser.add_argument('-a', type = int, required = False, help='reverses the string for every value given')
args = parser.parse_args()
#still need to encorporate arguments into program.



#reverse string function
def reverse_string(input):
    str = "" #placeholder
    for i in input:
        str = i + str
    return str #returns reversed string


#asks user input
input = input("Enter your string to be reversed: ")
#calls function with the input
mytxt = reverse_string(input)
#prints out the function
print(mytxt)
