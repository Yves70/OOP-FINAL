class SinigangNaBaboy:
    def __init__(self, meat, sour_ingredient, vegetables):
        self.meat = meat
        self._sour_ingredient = sour_ingredient
        self.__vegetables = vegetables

    def __str__(self):
        return f"Ang sinigang ko ay may {self.meat}, {self._sour_ingredient}, at {', '.join(self.__vegetables)}"

    def list_vegetables(self):
        return self.__vegetables

# Examples of Sinigang na Baboy
sinigang1 = SinigangNaBaboy("baboy", "sampalok", ["kangkong", "labanos", "sitaw"])
sinigang2 = SinigangNaBaboy("baboy", "bayabas", ["kangkong", "okra"])
sinigang3 = SinigangNaBaboy("baboy", "kamias", ["talong", "sitaw"])

print(sinigang1)
print(sinigang2)
print(sinigang3)

print("Gulay sa Sinigang 1:", sinigang1.list_vegetables())
print("Gulay sa Sinigang 2:", sinigang2.list_vegetables())
print("Gulay sa Sinigang 3:", sinigang3.list_vegetables())
