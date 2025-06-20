import socket

host = input("Masukkan domain (contoh: google.com): ")
try:
    ip = socket.gethostbyname(host)
    print(f"IP dari {host} adalah {ip}")
except:
    print("Gagal mendapatkan IP")
