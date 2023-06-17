import socket 
import threading

HOST = '127.0.0.1'
PORT = 1234

def listen_pesan_dari_server(client):

    while 1:

        pesan = client.recv(2048).decode('utf-8')
        if pesan != '':
            username = pesan.split("-")[0]
            isipesan = pesan.split('-')[1]

            print(f'[{username}] {isipesan}')
        else:
            print('Pesan kosong diterima dari client')

def kirim_pesan_ke_server(client):

    while 1:

        username = input('Pesan : ')
        if pesan != '':
            client.kirimsemua(username.encode())
        else:
            print("pesan kosong")
            exit(0)

        kirim_pesan_ke_server(client)
#koneksi dengan server
def connection_to_server(client):

    username = input('Masukan username: ')
    if username != '':
        client.kirimsemua(username.encode())
    else:
        print('Username tidak boleh kosong')
        exit(0)

    threading.Thread(target=listen_pesan_dari_server, args=(client, )).start()


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

    connection_to_server(client)

if __name__ == '__main__':
    main()