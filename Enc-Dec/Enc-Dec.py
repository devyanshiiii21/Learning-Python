import os


def encrypt():
    file_path = input('Enter the file path to be encrypted: ')
    if os.path.exists(file_path):
        with open("data.txt", "r") as file1:
            content = file1.read()

        list1 = []
        encrypt_list = []
        
        list1 = list(content)
        for i in list1:
            char = ord(i)
            char+=17
            encrypt_list.append(char)
        print(encrypt_list)
        
        with open("encrypted_file.txt","w") as file2:
            for j in encrypt_list:
                word = chr(j)
                file2.write(word)
            
        print(f"Your file is successfully encrypted {file2}")
    else:
        print("Wrong file path.")
  
def decrypt():
    file_path = input("Enter the file path to be decrypted: ")
    if os.path.exists(file_path):
        with open(file_path, "r") as file1:
            content = file1.read()

        list1 = []
        decrypt_list = []
        
        list1 = list(content)
        for i in list1:
            char = ord(i)
            char -= 17
            decrypt_list.append(char)
        print(decrypt_list)
        
        with open("decrypted_file.txt","w") as file2:
            for j in decrypt_list:
                word = chr(j)
                file2.write(word)
            
        print(f"Your file is successfully decrypted {file2}")
    
    else:
        print("Wrong file path.")

print("""Enter 1 to encrypt the file
Enter 2 to decrypt the file
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

