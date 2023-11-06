from ._anvil_designer import Form1Template
from anvil import *
import anvil.server
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
class Form1(Form1Template):
  File_text=""
  Count=0
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.

    self.init_components(**properties)


    # Any code you write here will run before the form opens.

  def button_1_click(self, **event_arg):
    """This method is called when the button is clicked"""
    Name=anvil.server.call('Compare')
    alert(Name)
    result=anvil.server.call('Compute_Result')
    self.text_box_1.text=result



  def file_loader_1_change(self, file, **event_args):
    """This method is called when a new file is loaded into this FileLoader"""
    self.Count=anvil.server.call('qcount',file=file)
    alert("Question Paper Uploaded Successfully....")
    self.button_1.text=str("Start Test")
    self.repeating_panel_1.items=app_tables.table_3.search()


  def text_area_1_change(self, **event_args):
    """This method is called when the text in this text area is edited"""
    pass
