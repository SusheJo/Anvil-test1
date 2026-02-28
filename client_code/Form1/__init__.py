from ._anvil_designer import Form1Template
from anvil import *
import anvil.server

class Form1(Form1Template):
    def __init__(self, **properties):
        self.init_components(**properties)

    def button_1_click(self, **event_args):
        # Volání funkce, která běží u vás v Dockeru/lokálně
        vysledek = anvil.server.call('pozdrav_z_lokalu', 'Uživateli')
        self.label_1.text = vysledek