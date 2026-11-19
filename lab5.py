class Sneakers:

    def __init__(self, brand="None", size=0, color="None", price=0, 
                 quantity=0, material="None", numberOfSales=0, 
                 etc="None"):
        self.brand = brand
        self.size = size
        self.color = color
        self.__price = price
        self.__quantity = quantity
        self.material = material
        self.__numberOfSales = numberOfSales
        self.etc = etc

    def __str__(self):
        return (f"{self.brand}: Ціна: {self.__price}, Розмір: {self.size}, " 
                f"Колір: {self.color}, Кількість: {self.__quantity}")

    @property
    def price(self):
        return self.__price

    @price.setter
    def price(self, val):
        if val < 0:
            print("Ціна від'ємна")
        else:
            self.__price = val

    @property
    def quantity(self):
        return self.__quantity

    @quantity.setter
    def quantity(self, val):
        if val < 0:
            print("Кількість від'ємна")
        else:
            self.__quantity = val

    @property
    def numofsale(self):
        return self.__numberOfSales

    @numofsale.setter
    def numofsale(self, val):
        if val < 0:
            print("Кількість продажів від'ємна")
        else:
            self.__numberOfSales = val

    def __del__(self):
        print(f"Кросівки {self.brand} видалено")


class SportShoesStore:

    def __init__(self):
        self.__store = []

    def add(self, shoe):
        self.__store.append(shoe)

    def sort_price(self):
        return sorted(self.__store, key=lambda shoe: shoe.price)

    def sort_quantity(self):
        return sorted(self.__store, key=lambda shoe: shoe.quantity)

    def sort_popular(self):
        return sorted(self.__store, key=lambda shoe: shoe.numofsale, reverse=True)

    def __str__(self):
        if not self.__store:
            return "Магазин порожній"

        shop = "Кросівки в наявності:\n"
        for shoe in self.__store:
            shop += f"{shoe}\n"
        return shop


def main():
    shoes1 = Sneakers(
        brand="Nike",
        size=42,
        color="Чорний",
        price=3500,
        quantity=15,
        material="Шкіра",
        numberOfSales=120,
        etc="Амортизація Air",
    )

    shoes2 = Sneakers(
        brand="Adidas",
        size=40,
        color="Білий",
        price=2000,
        quantity=25,
        material="Текстиль",
        numberOfSales=340,
        etc="Для бігу",
    )

    shoes3 = Sneakers(
        brand="Puma",
        size=45,
        color="Зелений",
        price=1200,
        quantity=14,
        material="Синтетика",
        numberOfSales=360,
        etc="Легка підошва",
    )

    shoes4 = Sneakers(
        brand="Asics",
        size=41,
        color="Синій",
        price=4100,
        quantity=32,
        material="Синтетика",
        numberOfSales=230,
        etc="Для залу",
    )
    
    shoesstore = SportShoesStore()

    shoesstore.add(shoes1)
    shoesstore.add(shoes2)
    shoesstore.add(shoes3)
    shoesstore.add(shoes4)

    print("Рейтинг за ціною")
    for shoe in shoesstore.sort_price():
        print(shoe)

    print()
    print("Рейтинг за кількістю")
    for shoe in shoesstore.sort_quantity():
        print(shoe)

    print()
    print("Топ найпопулярніших")
    for shoe in shoesstore.sort_popular():
        print(shoe)

    print()
    print(shoesstore)

    del shoes1, shoes2, shoes3, shoes4


if __name__ == "__main__":
    main()
  