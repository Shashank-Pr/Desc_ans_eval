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
    self.test_done.visible=True
    self.inst_panel.visible=True

  def test_done_click(self, **event_args):
    """This method is called when the button is clicked"""
    
    result=anvil.server.call('Compute_Result')
    self.result_box.visible=True
    self.result_box.text=result
    alert(f"Your result is {result} Marks.")

  

  def cred_done_click(self, **event_args):
    """This method is called when the button is clicked"""
    if(self.name_std.text==""):
      alert("Mention Your Name!")
    elif(self.roll_no.text==""):
      alert("Mention Your Roll no!")
    else:
      alert(f"{self.name_std.text},Roll no : {self.roll_no.text}, Upload your provided Question Paper...")
      self.label_2.visible=True
      self.file_loader_1.visible=True

  def exit_click(self, **event_args):
    """This method is called when the button is clicked"""
    app_tables.table_3.delete_all_rows()
    name=self.name_std.text
    rn=self.roll_no.text
    Mark=(self.result_box.text)
    app_tables.results.add_row(Name=name,Marks=Mark,Roll_no=rn)
    open_form('Form2')

  
   
    
    
    
