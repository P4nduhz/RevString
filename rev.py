#rev.py
print("|==================================================|")
print("|  _____             _____ _        _              |")
print("| |  __ \           / ____| |      (_)             |")
print("| | |__) |_____   _| (___ | |_ _ __ _ _ __   __ _  |")
print("| |  _  // _ \ \ / /\___ \| __| '__| | '_ \ / _` | |")
print("| | | \ \  __/\ V / ____) | |_| |  | | | | | (_| | |")
print("| |_|  \_\___| \_/ |_____/ \__|_|  |_|_| |_|\__, | |")
print("|                                            __/ | |")
print("|    By P4nduhz                             |___/  |")
print("|    github.com/PPanduhz                           |")
print("|==================================================|")
print()



import argparse

#create an ArgumentParser object
parser = argparse.ArgumentParser(description = 'Reverse a String')

#declare arguments
parser.add_argument('-s', action = 'store_true', help='removes spaces from the reversed string')
parser.add_argument('-a', type = int, default = 1, help='reverses the string for every value given')
args = parser.parse_args()



#reverse string function
def reverse_string(input):
    if args.s:
        input = input.replace(" ", "")
    str = ""
    for i in range(0, len(input), args.a):
        str = input[i:i+args.a] + str
    return str



#asks user input
input = input("Enter your string to be reversed: ")
if not input:
#if no input error message displayed
    print("No input provided. Please enter a valid string.")
else:
    #calls function with the input
    mytxt = reverse_string(input)
    #prints out the function
    print(mytxt)
