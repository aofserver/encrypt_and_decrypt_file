#pip install cryptography
import os
import time
from cryptography.fernet import Fernet

remove_status = False

def encrypt():
    global remove_status
    try:
        key = Fernet.generate_key()
        print("key : ",key)
        with open("key.txt", 'wb') as f:
            f.write(key)
        input_file = 'Username & Password.txt'
        output_file = 'Username & Password.encrypted'
        with open(input_file, 'rb') as f:
            data = f.read()
        fernet = Fernet(key)
        encrypted = fernet.encrypt(data)
        remove_status = True
        print("############### encrypted ##############")
        with open(output_file, 'wb') as f:
            f.write(encrypted)
    except:
        print("#### Request Username & Password.txt ####")

    # You can delete input_file if you want

def decrypt():
    global remove_status
    try:
        with open("key.txt", 'rb') as f:
            key = f.read()
        input_file = 'Username & Password.encrypted'
        output_file = 'Username & Password.txt'
        with open(input_file, 'rb') as f:
            data = f.read()
        fernet = Fernet(key)
        decrypted = fernet.decrypt(data)
        print(">>> ",str(decrypted)[2:12])
        if str(decrypted)[2:12] == "#"*10:
            remove_status = True
            print("############### decrypted haeder success ##############")
        else:
            remove_status = False
            print("############### decrypted haeder fail ##############")
        with open(output_file, 'wb') as f:
            f.write(decrypted)
    except:
        print("############ Request key.txt ############")

    # You can delete input_file if you want



def SafeDataFile(filename):
    global remove_status
    if os.path.exists(filename) and remove_status:
        with open(filename, 'w') as file:
            file.write('')
        os.remove(filename)
    

if __name__ == '__main__':
    hash_status = ''
    while True:
        print("1. Encrypt")
        print("2. Decryption")
        print("-- Press Q to exit. --")
        inputdata = input("Select method : ")
        if inputdata == "1":
            hash_status = True
            encrypt()
            print("##########################################")
        if inputdata == "2":
            hash_status = False
            decrypt()
            print("##########################################")
        if inputdata == "exit" or inputdata == "q" or inputdata == "Q":
            if hash_status and type(hash_status) != str:
                list_filename = ["Username & Password.txt"]
                for i in list_filename: 
                    SafeDataFile(i)
            if not hash_status and type(hash_status) != str:
                list_filename = ["Username & Password.encrypted","key.txt"]
                for i in list_filename:
                    SafeDataFile(i)
            break

