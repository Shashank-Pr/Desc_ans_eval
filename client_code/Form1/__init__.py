from ._anvil_designer import Form1Template
from anvil import *
import anvil.server
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
class Form1(Form1Template):
  
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.

    self.init_components(**properties)
    # Any code you write here will run before the form opens.

  
    

  def file_loader_1_change(self, file, **event_args):
    """This method is called when a new file is loaded into this FileLoader"""
    self.Count=anvil.server.call('qcount',file=file)
    alert("Question Paper Uploaded Successfully....")
    self.repeating_panel_1.items=app_tables.table_3.search()
    self.text_box_3.visible=True

  def button_2_click(self, **event_args):
    """This method is called when the button is clicked"""
    
    result=anvil.server.call('Compute_Result')
    self.text_box_1.text=result
