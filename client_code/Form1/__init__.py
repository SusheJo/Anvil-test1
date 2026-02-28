from ._anvil_designer import Form1Template
from anvil import *
import anvil.server

class Form1(Form1Template):
    def __init__(self, **properties):
        self.init_components(**properties)

    def button_1_click(self, **event_args):
        # 1. Zavoláme funkci z vašeho lokálního Pythonu
        # Musí to být uvnitř bloku try/except, abychom viděli, pokud selže spojení
        try:
            vysledek = anvil.server.call('pozdrav_z_windows')
            # 2. Teď je 'vysledek' definován a můžeme ho vypsat
            alert(vysledek)
        except Exception as e:
            alert(f"Chyba při volání lokálního Pythonu: {e}")