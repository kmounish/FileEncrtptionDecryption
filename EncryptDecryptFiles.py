from cryptography.fernet import Fernet

def encryptFile(file):
    #Generates key
    key = Fernet.generate_key()
    
    #Saves key a file called mykey.key
    with open("mykey.key",'wb') as mykey:
        mykey.write(key)
    
    with open(file, "rb") as original_file:
        original = original_file.read()
    
    #makes fernet object 
    f = Fernet(key)
    #encrypts the file data
    encrypted = f.encrypt(original)

    #writes the encrypted data in to the new file
    with open('En_'+file, 'wb') as encrypted_file:
        encrypted_file.write(encrypted)

def decryptFile(file, keyname):
    #Reads the key 
    with open(keyname, 'rb') as mykey:
        key = mykey.read()      
        key = key.decode('utf-8')
    
    with open(file, 'rb') as encrypted_file:
        encrypted = encrypted_file.read()
    
    f = Fernet(key)
    
    #decrypts the file data    
    decrypted = f.decrypt(encrypted)
    
    #writes it back in to the file
    with open(file, 'wb') as encrypted_file:
        encrypted_file.write(decrypted)


filename = input("Enter file name to be encrypted/decrypted: ")
option = int(input("Enter 1 to encrypt and 2 to decrypt: "))

if option == 1:
    encryptFile(filename)
elif option == 2:
    key = input("Enter the key filename: ")
    decryptFile(filename, key)
else:
    print("Entered an invalid option")
