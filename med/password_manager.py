from cryptography.fernet import Fernet
PASS_PATH = r"D:\code\mini_project\med\pass.txt"
"""def write_key(): 
    key = Fernet.generate_key()
    with open(r"D:\code\mini_project\med\key.key", "wb") as key_file:
        key_file.write(key)"""

def load_key():
    try:
        with open(r"D:\code\mini_project\med\key.key","rb") as file:
            key = file.read()
        return key
    except FileNotFoundError:
        print("Error: key.key file not found. Please run write_key() first.")
        exit()

master_pwd = input("What is the master password? ")
key = load_key()
fer = Fernet(key)

def add():
    name = input("Enter the account name: ")
    pwd = input("Enter the password: ")
    with open(PASS_PATH,"a") as f:
        f.write(name + "||" + fer.encrypt(pwd.encode()).decode() + "\n")
def view():
    try:
        with open(PASS_PATH,"r") as f:
            for line in f.readlines():
                data = line.rstrip()
                if not data:  # Skip empty lines
                    continue
                try:
                    user, passw = data.split("||")
                    decrypted_pwd = fer.decrypt(passw.encode()).decode()
                    print("User account: " + user + ", Password account: " + decrypted_pwd)
                except Exception as e:
                    print(f"Error decrypting entry: {data[:20]}... - {e}")
    except FileNotFoundError:
        print("No passwords saved yet.")
            
while True:
    mode = input("Would you like to add or view existing one (view , add) or press q to quit ").lower()
    if mode == "q":
        break
    if mode == "add":
        add()
    elif mode == "view":
        view()
    else :
        print("invalid mode")
        continue