chocolates=[
    {"name":"vanilla","amount":50,"stock":100},
    {"name":"strawberry","amount":30,"stock":500},
    {"name":"orange","amount":80,"stock":400},
    {"name":"blueberry","amount":20,"stock":700},
    {"name":"almond","amount":30,"stock":100}
]

def display(chocolates):
  for chocolate in chocolates:
    print("Name: ",chocolate['name'],"Amount: ",chocolate['amount'],"Stock: ",chocolate['stock'])