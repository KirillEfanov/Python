import json

class Footwear:

    def __init__(self, size, price):
        self.size = size
        self.price = price
        
    def Print(self):
        print("Размер: ", self.size)
        print("Цена: ", self.price)
