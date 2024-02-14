for i in range(10):
    print((i*2.6)%1)

class worker:
    def __init__(self,rate: int | float,price: int,name: str = "Generic Worker", description: str | None = None):
        self.rate = rate
        self.price = price
        self.name = name
        self.lore = description
        self.count: int = 0
        self.modifier: float = 1
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
    def buy(self, many: int = 1) -> float | int:
        priceToPay = self.getPrice(many)
        self.count += many
        return priceToPay
    def describe(self):
        if self.lore == None:
            return
        else:
            print(self.lore)
default = [
    worker(
        0.1,
        15,
        "Cursor",
        "Autoclicks once every 10 seconds (If you're using a real autoclicker that's cheating)"
        ),
    worker(
        1,
        100,
        "Grandparent",
        "Cooks cookies with love"
        ),
    worker(
        8,
        1100,
        "Garden",
        "Grows a variety cookie based plants from cookie seeds"
        ),
    worker(
        50,
        13000,
        "Mine",
        "Mines out cookie dough and chocolate chip deposits"
        ),
    worker(
        300,
        135000,
        "Factory",
        "Produces large quantities of cookies hot off the production line"
        ),
    worker(
        1400,
        1400000,
        "Bank",
        "Generates cookie equity from interest"
        ),
    worker(
        8000,
        21000000,
        "Monument",
        "Full of precious chocolate from times before even Grandparents"
        ),
    worker(
        45000,
        333000000,
        "Chemistry Lab",
        "Uses chemistry to artificially create cookies from strange chemicals that probably shouldn't be ingested"
        ),
    worker(
        250000,
        5000000000,
        "Magicworks",
        "Summons cookies with magical means"
        ),
    worker(
        1600000,
        75000000000,
        "Lunar Collector",
        "Brings in fresh cookies from cookie moons far far away"
        ),
    worker(
        10000000,
        1000000000000,
        "Cookie Accelerator",
        "Accelerates cookies into eachother very fast to create even more cookies"
        ),
    worker(
        65000000,
        14000000000000,
        "Wormhole",
        "Opens portals that lead to universes filled to the brim with cookies"
        ),
    worker(
        420000000,
        160000000000000,
        "Wishing Star",
        "Uses the power of wishes to wish cookies into existence"
        ),
    worker(
        3000000000,
        2300000000000000,
        "RNG Manipulation",
        "Generates cookies out of thin air through 'luck'"
        ),
    worker(
        21000000000,
        24500000000000000,
        "Fractal Engine",
        "Takes cookies and creates more cookies from those cookies"
        ),
    worker(
        150000000000,
        310000000000000000,
        "Time Machine",
        "Brings cookies from the past and future before they were eaten"
        ),
    worker(
        1000000000000,
        7000000000000000000,
        "Cortex Baker",
        "Planet sized beings that constantly imagine cookies into existence"
        ),
    worker(
        8700000000000,
        12000000000000000000,
        "Void Dimension",
        "A void dimension that can be used to store many more cookies, and in itself can make cookies"
        ),
    worker(
        64000000000000,
        1984000000000000000000,
        "Python Console",
        "Creates cookies from the very code this game was written in"
        ),
    worker(
        510000000000000,
        540000000000000000000000,
        "Clone Copy",
        "You alone are the reason behind all of these cookies, now imagine if there were more"
        ),
    worker(
        3400000000000000,
        340000000000000000000000000,
        "Idlemultiverse",
        "There's several other idle games running along side this one, and now you can hijack their multiverses and convert whatever they're making into cookies"
        ),
    worker(
        12345678900000000,
        999990000000000000000000000000,
        "Beyond",
        "An incomprehensible way to make even more cookies"
        ),
    worker(
        87000000000000000,
        6410000000000000000000000000000000,
        "Infinity Cookie",
        "Siphons cookies right out of infinity itself, making for an almost unlimited source of cookies"
        ),
    worker(
        922337203685477807,
        340282366920938463463374607431768211456,
        "Overflowinator",
        "Fills in all the empty spaces in existence with cookies, and then makes even more cookies"
        ),
    worker(
        79000000000000000000,
        100000000000000000000000000000000000000000000000000,
        "Omega Black Hole Bomb",
        "Takes full advantage of black holes with the mass of several multiverses and converts it all into cookies"
        ),
    worker(
        0,
        10000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000,
        "Zero",
        "The very final thing this game can give you. If you've managed to buy even at least one of these, then you win."
        )
    ]