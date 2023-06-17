import socket
import threading

HOST = '127.0.0.1'
PORT = 1234  # Silahkan sesuaikan port 0 sampai 65535
LISTENER_LIMIT = 5
client_aktif = [] # jumlah keseluruhan client aktif


# Merespon pesan yang akan datang
def pesan(client, username):

    while 1: 
        pesan = client.recv(2048).decode('utf-8')
        if pesan !='':

            isi_pesan = username + '-' + pesan
            kirim_semua_pesan((isi_pesan))

        else:
            print(f'Pesan kosong dikirim dari {username} client')

# mengirim pesan ke satu client

def kirim_pesan(client, pesan):

    client.kirimsemua(pesan.encode())

# untuk mengirimkan semua pesan ke client apabila terhubung dengan server 
def kirim_semua_pesan(from_username, pesan):
    
    for user in client_aktif:  

        kirim_pesan(user[1], pesan)

# handle client
def client_hand(client):

    # Server akan merespon pesan yang dikirim
    # Sesuai dengan username 
    while 1: 

        username = client.recv(2048).decode('utf-8')
        if username != '':
            client_aktif.append(username, client)
            break
        else:
            print('Terdapat kendala')
    threading.Thread(target=pesan, args=(client, username, )).start()

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

        threading.Thread(target=client_hand, args=(client, )).start()
if __name__ == '__main__':
    main()
