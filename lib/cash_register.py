#!/usr/bin/env python3

class CashRegister:
  def __init__(self):
    self.discount = 0
    self.total = 0
    self.items = []
    self.previous_transactions = []
  
  @property
  def discount(self):
    return self._discount
  
  @discount.setter
  def discount(self,value):
    if type(value) is not int or not 0 <= value <= 100:
      print("Not valid discount")
    self._discount = value

  def add_item(self,item,price,quantity):
    self.total += price * quantity
    self.items.append(item)
    self.previous_transactions.append({
      "item": item,
      "price": price,
      "quantity": quantity
    })
  
  def apply_discount(self):
    return (self.total * self.discount)/100
  
register = CashRegister()
itm_1 = register.add_item("sugar",100,20)
print(register.items)
print(register.total)