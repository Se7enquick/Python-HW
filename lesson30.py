
class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price
    

 
class Costumer(Product):
    def __init__(self, money):
        self.money = money

    def counter(self, prod):
        result = self.money / prod.price
        return int(result)

class VipCostumer(Costumer):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        
    
    
    def counter(self, prod):
        result = super().counter(prod) / 0.8
        return int(result)


class SuperCostumer(VipCostumer):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)


    def counter(self,prod):
        result = super().counter(prod) / 0.8
        return int(result)


check = Product(name='Milk', price=10)
ivan = Costumer(money=200)
oksana = VipCostumer(money=200)
sheikh = SuperCostumer(money=200)
print(ivan.counter(check))
print(oksana.counter(check))
print(sheikh.counter(check))
