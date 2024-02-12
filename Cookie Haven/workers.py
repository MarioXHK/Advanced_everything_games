print(1, end = "")
for i in range(50):
    print(0, end = "")
print()
class worker:
    def __init__(self,rate: int | float,price: int,name: str = "Generic Worker", description: str | None = None):
        self.rate = rate
        self.price = price
        self.name = name
        self.lore = description
        self.count: int = 0
        self.modifier: float = 0
        self.adder: int = 0
        self.postAdder: int = 0
    def giveCookies(self) ->  int | float:
        return (self.rate*self.modifier+self.adder)*self.count+self.postAdder
    def getPrice(self, many: int = 1, discount: float = 1.0) -> int:
        if many < 1:
            return 0
        newPrice = self.price*1.15**self.count
        if many > 1:
            for i in range(2,many):
                newPrice += self.price*1.15**(self.count + i)
        return int(newPrice*discount)
    def buy(self, many: int = 1):
        self.count += many
    def describe(self):
        if self.lore == None:
            return
        else:
            print(self.lore)