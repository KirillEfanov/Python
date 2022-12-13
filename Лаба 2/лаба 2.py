import json

class Footwear:

    def __init__(self, size, price):
        self.size = size
        self.price = price
        
    def Print(self):
        print("Размер: ", self.size)
        print("Цена: ", self.price)
        
    def json_save(self, json_filepath: str):
        to_json = {
            "size": self.size,
            "price": self.price
        }
        with open(json_filepath, 'w') as file:
            json.dump(to_json, file)
