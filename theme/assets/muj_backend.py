import anvil.server
import time

# POUŽIJTE PŘESNĚ TOTO:
URL = "ws://127.0.0.1:3030/_/uplink"
KLIC = "moje_heslo_123"

print(f"Pokus o připojení k Anvil Dockeru na {URL}...")

while True:
    try:
        anvil.server.connect(KLIC, url=URL)
        print("--- SPOJENÍ ÚSPĚŠNĚ NAVÁZÁNO ---")
        break
    except Exception as e:
        print(f"Chyba: {e}. Zkouším to znovu za 5 sekund...")
        time.sleep(5)

@anvil.server.callable
def pozdrav_z_windows():
    return "Ahoj z tvého Pythonu ve Windows 11!"

anvil.server.wait_forever()

try:
    print("Uplink je aktivní. Pro ukončení stiskni Ctrl+C.")
    anvil.server.wait_forever()
except KeyboardInterrupt:
    print("\nUplink byl bezpečně ukončen uživatelem.")