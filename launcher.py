import os
import time

def animate_text(text, delay=0.1):
    current = ""
    for char in text:
        current += char
        print("......."+current)
        time.sleep(delay)
    return current

os.system("clear")
print("Connecting....")
time.sleep(1)

print()
animate_text("YANOFFICIALID TOOLS", 0.08)
print("🔰 YANOFFICIALID TOOLS 🔰\n")
time.sleep(0.5)

print("🧠 Developer: @YanOfficialID")
print("📞 CS: Now coming online...\n")
time.sleep(0.5)

print("┌─[ MENU TOOLS ]─┐")
print("│ 1. DDOS WEBSITE")
print("│ 2. CEK IP WEB")
print("│ 3. STATUS TOOLS")
print("└────────────────┘")

menu = input("\nPilih menu (1/2/3): ")

if menu == "1":
    os.system("python ddos.py")
elif menu == "2":
    os.system("python cekip.py")
elif menu == "3":
    os.system("python status.py")
else:
    print("Pilihan tidak valid.")
