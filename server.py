import socket
import threading

HOST = '127.0.0.1'
PORT = 1234  # Silahkan sesuaikan port 0 sampai 65535
LISTENER_LIMIT = 5

# Fungsi utama
def main():
    # Membuat server socket dengan class object
    # AF_INET: kita gunakan untuk alamat IPv4
    # SOCK_STREAM: kita gunakan untuk menggunkan TCP packets untuk komunikasi
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    try:
        # Host IP and PORT
        server.bind((HOST, PORT))
        print(f'Server berjalan pada {HOST} {PORT}')
    except:
        print(f'Tidak dapat meraih host {HOST} dan port {PORT}')
        return

    # Pengaturan limit server
    server.listen(LISTENER_LIMIT)

    # perulangan untuk tetap terhubung dengan koneksi ke client.py
    while 1:
        client, address = server.accept()
        print(f'Sukses terhubung dengan client {address[0]} {address[1]}')

if __name__ == '__main__':
    main()
