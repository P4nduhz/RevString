#rev.py                                      
def reverse_string(x):
  return x[::-1]

input = input("Enter your string to be reversed: ")
mytxt = reverse_string(input)
print(mytxt)
