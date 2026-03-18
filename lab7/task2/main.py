from models import Vehicle, Car, Bike


def main():

    vehicle = Vehicle("Generic", 2020, "Vehicle")
    my_car = Car("Toyota", 2022, "Camry")
    my_bike = Bike("BMX", 2021)

    my_vehicles = [vehicle, my_bike, my_car]

    for i in my_vehicles:
        print(i)
        print(i.get_info())
        print(i.move())

        if isinstance(i, Car):
            print(f"Signal: {i.signal()}")
        elif isinstance(i, Bike):
            print(f"Signal: {i.signal()}")


if __name__ == "__main__":
    main()