import re 
string = "a b c d e f g "
regex = re.compile("((\w+)\s+\w+)")
print(regex.findall(string))
print("***********\n")
regex = re.compile("(\w+)")
print(regex.findall(string))
print("***********\n")
regex = re.compile("\w+\s+")
print(regex.findall(string))