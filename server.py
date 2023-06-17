import socket
import threading

HOST = '127.0.0.1'
PORT = 1234
LISTENER_LIMIT = 5
client_aktif = []  # Jumlah keseluruhan client aktif

# Merespon pesan yang akan datang
def pesan(client, username):
    while True:
        try:
            pesan = client.recv(2048).decode('utf-8')
            if pesan != '':
                isi_pesan = username + '-' + pesan
                kirim_semua_pesan(username, isi_pesan)
            else:
                print(f'Pesan kosong dikirim dari {username} client')
        except ConnectionResetError:
            print(f'Koneksi dengan {username} ditutup secara paksa.')
            client_aktif.remove((username, client))
            break

# Mengirim pesan ke satu client
def kirim_pesan(client, pesan):
    client.sendall(pesan.encode())

# Mengirim semua pesan ke client yang terhubung dengan server
def kirim_semua_pesan(from_username, pesan):
    for user in client_aktif:
        try:
            kirim_pesan(user[1], pesan)
        except ConnectionResetError:
            print(f'Koneksi dengan {user[0]} ditutup secara paksa.')
            client_aktif.remove(user)

# Handle client
def client_hand(client):
    while True:
        try:
            username = client.recv(2048).decode('utf-8')
            if username != '':
                client_aktif.append((username, client))
                break
            else:
                print('Terdapat kendala')
        except ConnectionResetError:
            print('Koneksi ditutup secara paksa.')
            break
    threading.Thread(target=pesan, args=(client, username,)).start()

# Fungsi utama
def main():
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    try:
        server.bind((HOST, PORT))
        print(f'Server berjalan pada {HOST} {PORT}')
    except Exception as e:
        print(f'Tidak dapat meraih host {HOST} dan port {PORT}: {str(e)}')
        return

    server.listen(LISTENER_LIMIT)

    while True:
        client, address = server.accept()
        print(f'Sukses terhubung dengan client {address[0]} {address[1]}')

        threading.Thread(target=client_hand, args=(client,)).start()

if __name__ == '__main__':
    main()
