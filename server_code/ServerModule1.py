import anvil.email
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
import anvil.server
import json

# This is a server module. It runs on the Anvil server,
# rather than in the user's browser.
#
# To allow anvil.server.call() to call functions here, we mark
# them with @anvil.server.callable.
# Here is an example - you can replace it with your own:
#
@anvil.server.callable
def say_hello(name):
  return ("Hello, " + name + "!")

@anvil.server.callable
def qcount(file):
  a=file.get_bytes()
  obj=json.loads(a)
  qcnt=str(len(obj))
  x=len(obj)
  for i in range (1,x+1):
    Number=str(i)
    app_tables.table_3.add_row(Questions=obj[Number]['Question'])
  return qcnt
@anvil.server.callable
def Compute_Result():
  info = [
  {
   'Question': r['Questions'],
   'Ans': r['Answer'],
  }
  for r in app_tables.table_3.search()
  ]
  result=anvil.server.call('Result',info)
  return result
