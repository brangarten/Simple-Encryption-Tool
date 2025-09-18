from cryptography.fernet import Fernet
import os
    
show_key = False
key_holder = "blablabla"

# Initial phase before going into main loop
# Purpose is to generate a private key for the users encryption/decryption cases
# Keys can then be distributed to others or stored to decrypt certain messages
def key_prompt():
    global key_holder
    print("Please select an option:")
    
    userInput = int(input("1. Enter Key \n2. Generate Key \n> "))
    match userInput:
        # Not working right now
        # Will fix later, not now in this moment because I'm going to eat
        case 1:
            os.system('cls')
            key = input("Enter your key: ")
            return Fernet(key)
        case 2:
            os.system('cls')
            key = Fernet.generate_key()
            key_holder = key
            return Fernet(key)

def print_menu():
    print("Key: ", end='')
    if show_key == True:
        print(key_holder)
    else:
        print('•'*len(key_holder))
    print("1. Encrypt \n2. Decrypt \n3. Swap Key \n4. Show Key \n5. Quit")
    print(show_key)
    
def fetch_message():
    # encode used to convert str -> bytes
    # Why? Fernet functions parameters passes through bytes, not strings
    return input("Enter message: ").encode()

def encrypt(msg):
    return key.encrypt(msg)

def decrypt(msg):
    return key.decrypt(msg)    

def swap_key():
    print("Meow")
    
def reveal_key():
    global show_key
    
    #If true then false, if not true then true
    if show_key == True:
        show_key = False
    else:
        show_key = True

# Main Program
def main():
    while True:
        print_menu()
        userInput = int(input("Select an Option \n> "))

        match userInput:
            case 1: 
                message = fetch_message()
                print(encrypt(message))
                input()
            case 2:
                message = fetch_message()
                print(decrypt(message))
                input()
            case 3:
                print("I'll do this later :3")
            case 4:
                reveal_key()
            case 5:
                break
            
        os.system('cls')

if __name__ == "__main__":
    key = key_prompt()
    main()
