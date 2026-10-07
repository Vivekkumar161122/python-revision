class Laptop:
    storage_type = "ssd"

    def __init__(self, RAM, storage):
        self.RAM = RAM
        self.storage = storage

    @classmethod
    def get_storage_type(cls):
        print(f"storage type = {cls.storage_type}")

    def get_info(self):  # instance method
        print(f"laptop has {self.RAM} RAM & {self.storage} {Laptop.storage_type}")

    @staticmethod
    def calc_discount(price, discount):
        final_persent = price - (discount * price / 100)
        print(f"discounted price = {final_persent}")


l1 = Laptop("16gb", "512gb")
l1.calc_discount(40_000, 10)
