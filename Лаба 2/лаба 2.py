import json

class Footwear:

    def __init__(self, size, price):
        self.size = size
        self.price = price
        
    def __repr__(self):
        return "Размер: % s, Цена: % s" % (self.size, self.price)
        
    def json_save(self, json_filepath: str):
        to_json = {
            "size": self.size,
            "price": self.price
        }
        with open(json_filepath, 'w') as file:
            json.dump(to_json, file)
            
    def json_load(self, json_filepath: str):
        with open(json_filepath) as f:
            a = json.load(f)
            self.size = a["size"]
            self.price = a["price"]
    
class Manufacturer(Footwear):

    def __init__(self, size, price, country):
        super().__init__(size, price,)
        self.country = country
        
    def __repr__(self):
        return "Размер: % s, Цена: % s, Страна: % s" % (self.size, self.price, self.country)
        
    def json_save(self, json_filepath: str):
        to_json = {
            "size": self.size,
            "price": self.price,
            "country": self.country
        }
        with open(json_filepath, 'w') as file:
            json.dump(to_json, file)
            
    def json_load(self, json_filepath: str):
        with open(json_filepath) as f:
            a = json.load(f)
            self.size = a["size"]
            self.price = a["price"]
            self.country = a["country"]

            
boots = Manufacturer(50, 40000, "Germany")
print(boots)
boots.json_save("data.json")
sneakers = Manufacturer(0, 0, " ")
sneakers.json_load("data.json")
print(sneakers)
