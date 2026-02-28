from ._anvil_designer import Form1Template
from anvil import *
import anvil.server

class Form1(Form1Template):
    def __init__(self, **properties):
        self.init_components(**properties)

    # ŽÁDNÉ @handle! Anvil si to pohlídá sám.
    def button_1_click(self, **event_args):
        print("Tlačítko bylo stisknuto v prohlížeči")
        try:
            # Voláme funkci 'pozdrav_z_windows' ve vašem PC
            vysledek = anvil.server.call('pozdrav_z_windows')
            self.label_1.text = vysledek
        except Exception as e:
            alert(f"Chyba při volání lokálního Pythonu: {e}")

    def button_2_click(self, **event_args):
        print("Tlačítko 2 bylo stisknuto")
        pass