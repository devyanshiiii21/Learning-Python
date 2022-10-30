
def encrypt():
    file1 = open("data.txt", "r")
    content = file1.read()

    l = len(content)

    list1 = list(content)
    for i in list1[0 : l]:
         char = ord(list1[i])
         char+=1
         list1 = chr(char)
    return list1

def decrypt():
    pass


print("""Enter 1 to encrypt
Enter 2 to decrypt
Enter 3 to exit""")
ch = input("Enter your choice: ")

if ch == '1':
    encrypt()
elif ch == '2':
    decrypt()
elif ch == '3':
    exit(1)
else:
    print('Wrong Choice entered')

