a = input("Please enter a 4 character string : ")
b = ''

for i in a :
    if ord(i) >=90:
        i = chr(ord(i)-32)
        b = b + i

print("The string capitalization is",b)
