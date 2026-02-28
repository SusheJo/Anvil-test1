from ._anvil_designer import Form1Template
from anvil import *

class Form1(Form1Template):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    # Any code you write here will run before the form opens.

  @handle("button_1", "clicked")
  def button_1_click(self, **event_args):
      """This method is called when the button is clicked"""
      pass

  @handle("text_box_1", "pressed_enter")
  def text_box_1_pressed_enter(self, **event_args):
      """This method is called when the user presses Enter in this text box"""
      pass
