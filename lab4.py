class Automobile:
    def __init__(self, engine_power = 100, brand = "Невідома", max_speed = 180, year = 2020, color = "Білий"):
        self.__engine_power = engine_power
        self.__brand = brand
        self.__max_speed = max_speed
        self.year = year
        self.color = color

    def get_engine_power(self):
        return self.__engine_power

    def get_brand(self):
        return self.__brand

    def get_max_speed(self):
        return self.__max_speed

    def __str__(self):
        return (
            f"Марка: {self.__brand}, "
            f"потужність: {self.__engine_power} к.с., "
            f"максимальна швидкість: {self.__max_speed} км/год, "
            f"рік випуску: {self.year}, "
            f"колір: {self.color}"
        )

    def __repr__(self):
        return (
            f"Automobile(engine_power = {self.__engine_power}, "
            f"brand ='{self.__brand}', "
            f"max_speed = {self.__max_speed}, "
            f"year = {self.year}, color = '{self.color}')"
        )

    def __del__(self):
        print(f"Об'єкт автомобіля {self.__brand} видалено.")


def main():
    car1 = Automobile(150, "BMW", 240, 2022, "Чорний")

    car2 = Automobile(120, "Toyota", 200, 2021, "Білий")

    car3 = Automobile()
    car3.color = "червоний"
    cars = [car1, car2, car3]

    for i, car in enumerate(cars, start = 1):
        print(f"\nАвтомобіль №{i}")
        print(f"Потужність двигуна: {car.get_engine_power()} к.с.")
        print(f"Марка: {car.get_brand()}")
        print(f"Максимальна швидкість: {car.get_max_speed()} км/год")
        print(f"Рік випуску: {car.year}")
        print(f"Колір: {car.color}")

    print("\nМетод __str__:")
    print(car1)

    print("\nМетод __repr__:")
    print(repr(car1))


if __name__ == "__main__":
    main()