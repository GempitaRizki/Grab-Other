import socket
import threading

HOST = '127.0.0.1'
PORT = 1234

def listen_pesan_dari_server(client):
    while True:
        pesan = client.recv(2048).decode('utf-8')
        if pesan != '':
            username = pesan.split("-")[0]
            isipesan = pesan.split('-')[1]
            print(f'[{username}] {isipesan}')
        else:
            print('Pesan kosong diterima dari server')

def kirim_pesan_ke_server(client):
    while True:
        pesan = input('Pesan: ')
        if pesan != '':
            client.sendall(pesan.encode())
        else:
            print("Pesan kosong")
            exit(0)

def connection_to_server(client):
    username = input('Masukkan username: ')
    if username != '':
        client.sendall(username.encode())
    else:
        print('Username tidak boleh kosong')
        exit(0)

    threading.Thread(target=listen_pesan_dari_server, args=(client,)).start()
    kirim_pesan_ke_server(client)

def main():
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    try:
        client.connect((HOST, PORT))
        print('Berhasil terhubung ke server')
    except Exception as e:
        print(f"Tidak dapat terhubung ke server {HOST} {PORT}: {str(e)}")
        return

    connection_to_server(client)

if __name__ == '__main__':
    main()
