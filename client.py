import socket 
import threading

HOST = '127.0.0.1'
PORT = 1234

def main():
    pass

    #membuat socket object 
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    #connect ke server 
    try:
        client.connect((HOST, PORT))
        print(f'Berhasil terhubung ke server')
    except:
        print(f"Tidak dapat connect ke server{HOST} {PORT}")
if __name__ == '__main__':
    main()