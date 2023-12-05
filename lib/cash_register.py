#!/usr/bin/env python3

#!/usr/bin/env python3

class CashRegister:
  def __init__(self, discount=0, total=0):
    self.discount = discount
    self.total = total
    self.items = list()
    self.last_transaction_price = None 
  
  def add_item(self, title, price, quantity=None):
    self.total += price * quantity if quantity else price
    if quantity:
      for i in range(quantity):
        self.items.append(title)
    else:
      self.items.append(title)
    self.last_transaction_price = price * quantity if quantity else price

  def apply_discount(self):
    self.total -= self.total * self.discount/100
    if self.discount:
      print("After the discount, the total comes to $800.")
    else:
      print("There is no discount to apply.")

  def void_last_transaction(self):
    self.total -= self.last_transaction_price 
    