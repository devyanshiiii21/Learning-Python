
def encrypt():
    file1 = open("data.txt", "r")
    content = file1.read()

    list1 = []
    encrypt_list = []

    list1 = list(content)
    for i in list1:
         char = ord(i)
         char+=23
         encrypt_list.append(char)
    print(encrypt_list)
    

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

