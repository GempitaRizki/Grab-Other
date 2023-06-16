import socket
import threading

HOST = '127.0.0.1'
PORT = 1234 #Silahkan sesuiakan port 0 sampai 65535
LISTENER_LIMIT = 5

#Fungsi utama 

def main():
    # Membuat server socker dengan class object
    # AF_INET : kita gunakan untuk alamat IPv4 
    # SOCK_STREAM : kita gunakan untuk menggupakan TCP packets untuk komunikasi
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    try: 
        #host IP and PORT 
        server.bind((HOST, PORT))
    except:
        print('Tidak dapat meraih host {HOST} dan port {PORT}')

    # Pengaturan limit server
    server.listen(LISTENER_LIMIT)

# perulangan untuk tetap terhubung dengan koneksi ke client.py
while 1: 
    client, address = server.accept()
    print('Sukses terhubung dengan client {address[0]} {address[1]}')

if __name__ == '__main__':
    main()