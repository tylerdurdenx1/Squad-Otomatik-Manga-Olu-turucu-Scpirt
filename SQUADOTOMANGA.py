import keyboard
import time
import threading
import pyperclip
from colorama import init, Fore, Style

init()

print("👋 Squad Otomatik Manga Oluşturucu'na Hoş Geldiniz!")
print("👨‍💻 Coder: TYLER DURDEN\n")
print(Fore.GREEN + "DİSCORD:tylerrdurrden" + Style.RESET_ALL)

print(Fore.RED + "⚠️ Lütfen oyunun ayarlarından konsol tuşunu F11 olarak ayarlayın." + Style.RESET_ALL)


manga_adi = input("📌 Hangi mangayı açmak istiyorsunuz? (Örn: m1a1): ").strip()
komut = f"CreateSquad {manga_adi} 1"
pyperclip.copy(komut)

print("\n✅ Manga komutu kopyalandı.")
print("▶️ Squad oyununu açın ve F5 tuşuna basarak otomasyonu başlatabilirsiniz.")
print("⚠️ Program Arkada Çalışacaktır Programda Olmanıza Gerek Yoktur.")
print("⏹️ Otomasyonu durdurmak için tekrar F5 tuşuna basın.")
print("🔄 Yeni bir manga oluşturmak için programı yeniden başlatmanız gerekmektedir.\n")

aktif = False 

def otomasyon():
    global aktif
    while True:
        if aktif:
           #BURAYA SİZİN KONSOLUNUZ HANGİ TUŞSA ONU YAZMANIZ YETERLİ 
            keyboard.press_and_release('F11')
            time.sleep(0.1)

            keyboard.press_and_release('ctrl+v')
            time.sleep(0.05)

    
            keyboard.press_and_release('enter')
            time.sleep(0.1)
        else:
            time.sleep(0.1)

def toggle_aktif():
    global aktif
    aktif = not aktif
    if aktif:
        print("✅ Otomasyon başlatıldı.")
        print("ℹ️ Yeni bir manga açmak için programı yeniden başlatmanız gerekmektedir.")
    else:
        print("⏹️ Otomasyon durduruldu.")

keyboard.add_hotkey('f5', toggle_aktif)

threading.Thread(target=otomasyon, daemon=True).start()

keyboard.wait()
