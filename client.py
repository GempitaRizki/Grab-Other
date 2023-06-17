import socket
import threading
import tkinter as tk
from tkinter import scrolledtext
from tkinter import messagebox

DARK_GREY = '#121212'
MEDIUM_GREY = '#1F1B24'
OCEAN_BLUE = '#464EB8'
WHITE = "white"
FONT = ("Helvetica", 17)
BUTTON_FONT = ('Helvetica', 15)
SMALL_FONT = ("Helvetica", 13)

def add_pesan(pesan):
    latar_pesan.config(state=tk.NORMAL)
    latar_pesan.insert(tk.END, pesan + '\n')
    latar_pesan.config(state=tk.DISABLED)

def connect():
    try:
        # CONNECT KE SERVER
        global client  # Menandai variabel sebagai global
        client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        client.connect((HOST, PORT))
        print('Berhasil terhubung ke server')
        add_pesan('[SERVER] Berhasil terhubung ke server')
    except:
        messagebox.showerror("Tidak dapat terhubung ke server", f"Tidak dapat terhubung ke server {HOST} {PORT}")

    username = username_textbox.get()
    if username != '':
        client.sendall(username.encode())
    else:
        messagebox.showerror('Username tidak valid', 'Username tidak boleh kosong')

    threading.Thread(target=listen_pesan_dari_server, args=(client,)).start()

    username_textbox.config(state=tk.DISABLED)
    tombol_username.config(state=tk.DISABLED)

def kirim_pesan():
    pesan = pesan_textbox.get()
    if pesan != '':
        client.sendall(pesan.encode())
        latar_pesan.delete(0, len(pesan))

    else:
        messagebox.showerror("Pesan kosong", "Pesan tidak boleh kosong")

root = tk.Tk()
root.geometry("600x600")
root.title("Pesan")
root.resizable(False, False)

root.grid_rowconfigure(0, weight=1)
root.grid_rowconfigure(1, weight=4)
root.grid_rowconfigure(2, weight=1)

top_frame = tk.Frame(root, width=600, height=100, bg=DARK_GREY)
top_frame.grid(row=0, column=0, sticky=tk.NSEW)

middle_frame = tk.Frame(root, width=600, height=400, bg=MEDIUM_GREY)
middle_frame.grid(row=1, column=0, sticky=tk.NSEW)

buttom_frame = tk.Frame(root, width=600, height=100, bg=DARK_GREY)
buttom_frame.grid(row=2, column=0, sticky=tk.NSEW)

nama_username = tk.Label(top_frame, text='Masukan username:', font=FONT, bg=DARK_GREY, fg=WHITE)
nama_username.pack(side=tk.LEFT, padx=5)

username_textbox = tk.Entry(top_frame, font=SMALL_FONT, bg=MEDIUM_GREY, fg=WHITE)
username_textbox.pack(side=tk.LEFT, padx=(0, 5), fill=tk.X, expand=True)

tombol_username = tk.Button(top_frame, text='Masuk', font=BUTTON_FONT, bg=OCEAN_BLUE, fg=WHITE, command=connect, width=10)
tombol_username.config(font=("Helvetica", 13))
tombol_username.pack(side=tk.LEFT)

pesan_textbox = tk.Entry(buttom_frame, font=FONT, bg=MEDIUM_GREY, fg=WHITE, width=38)
pesan_textbox.pack(side=tk.LEFT, padx=10)

tombol_pesan = tk.Button(buttom_frame, text='Kirim', font=BUTTON_FONT, bg=OCEAN_BLUE, fg=WHITE, command=kirim_pesan)
tombol_pesan.pack(side=tk.LEFT, padx=10)

latar_pesan = scrolledtext.ScrolledText(middle_frame, font=SMALL_FONT, bg=MEDIUM_GREY, fg=WHITE, width=67, height=23)
latar_pesan.config(state=tk.DISABLED)
latar_pesan.pack(side=tk.TOP)

HOST = '127.0.0.1'
PORT = 1234

def listen_pesan_dari_server(client):
    while True:
        pesan = client.recv(2048).decode('utf-8')
        if pesan != '':
            username = pesan.split("-")[0]
            isipesan = pesan.split('-')[1]
            add_pesan(f'[{username}] {isipesan}')
        else:
            messagebox.showerror('Error', 'Pesan kosong diterima dari server')

def main():
    root.mainloop()

if __name__ == '__main__':
    main()
