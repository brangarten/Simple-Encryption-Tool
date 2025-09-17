from cryptography.fernet import Fernet
import os
    
#top level

# Note: You can set the int len for fernets key generation. For my sake it's at 16

private_key = 0
key_cases   = 0
hide_key    = True
message     = ""

while True:
    # Prompt user if they want to gen or enter key
    # Change var name later
    userInput = int(input("1. Enter Private Key \n2. Generate a Private Key \n> "))
    
    if userInput == 1:
        os.system('clear')        
        private_key = input('Enter your Private Key \n> ')
        break
    elif userInput == 2:
        private_key = Fernet.generate_key()
        break
    else:
        print("Invalid Command")
        
key_cases = Fernet(private_key)
    
def display_menu():

    print("Ecryption Thingy".expandtabs(tabsize=10))
    print("Private Key: ".expandtabs(tabsize=5), end='')
    
    if hide_key == True:
        print('*' * len(private_key))
    elif hide_key == False:
        print(private_key)
        
    # ------------------------ #
    print('-'*60)
    print("1. Encrypt \n2. Decrypt \n3. Change Key \n4. Show/Hide Key \n5. Quit", end='\n')
    userInput = int(input('> '))
    
    match userInput:
        case 1:
            print("ec")
            encrypt()
        case 2:
            decrypt()
        case 3:
            hide_key = change_key()
        case 4:
            reveal_key()
        case 5:
            quit()
            

def encrypt():
    message = fetch_message()
    #token = key_cases.encrypt(message)
    print(f"Encrypted:")

def decrypt():
    token = fetch_token()
    print("Decrypted: " + key_cases.decrypt(token))
    
def reveal_key():
    if hide_key == False: 
        return True
    elif hide_key == True: 
        return False
        
def change_key():
    print("Finish Later")

def fetch_message():
    return input("Enter your message: ")

def fetch_token():
    return input("Enter your token: ")

def main():
    display_menu()
    
    

   
    
if __name__ == "__main__":
    main()
    
    
