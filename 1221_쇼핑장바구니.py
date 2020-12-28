class Basket:
    def __init__(self, id):
        self.id = id
        self.items = []
        self.prices = []
        self.quantity = []
        self.total = 0
        self.noitems = 0

    def add(self, item, price, qty):
        self.items.append(item)
        self.prices.append(price)
        self.quantity.append(qty)
        self.total += price * qty
        self.noitems += 1

    def delete(self, item, qty):
        for i in range(self.noitems):
            if item == self.items[i]:
                self.quantity[i] -= qty
                self.total -= self.prices[i] * qty

                if self.quantity[i] == 0:
                    self.noitems -= 1
                    del self.items[i]
                    del self.quantity[i]
                    del self.prices[i]
                break

    def printitems(self):
        print(self.id+"의 장바구니")
        for i in range(self.noitems):
            print(self.items[i], self.prices[i], self.quantity[i])
        print("** total =", self.total, ", noitems = ", self.noitems)

cjBasket = Basket("영희")
jsBasket = Basket("철수")

cjBasket.add("바나나", 5000, 2)
cjBasket.add("우유", 2500, 1)

jsBasket.add("라면", 5900, 1)
jsBasket.add("커피", 5000, 1)

print(" ")
cjBasket.printitems( )
print(" ")
jsBasket.printitems( )

print(" ")
cjBasket.delete("바나나", 1)
cjBasket.printitems( )

print(" ")
jsBasket.delete("라면", 1)
jsBasket.printitems( )
