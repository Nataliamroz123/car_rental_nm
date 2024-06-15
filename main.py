from models.data_source import rental_cars
from utils.crud import read_car_rental, add_car_rental, remove_car_rental, update_car_rental
from utils.emap import single_map


if __name__ == '__main__':
    while True:
        print("Welcome to the menu  ")
        print("0. Exit ")
        print("1. Read a list of car rental ")
        print("2. Add new car rental")
        print("3. Remove car rental")
        print("4. Update car rental")
        print("5. Generate map")
        print("6. Generate full map")
        menu_option = input("Choose an option:")
        if menu_option == "0":
            break
        if menu_option == "1":
            read_car_rental(rental_cars)
        if menu_option == "2":
            add_car_rental(rental_cars)
        if menu_option == "3":
            remove_car_rental(rental_cars)
        if menu_option == "4":
            update_car_rental(rental_cars)
        if menu_option == "5":
            single_map(read_car_rental(rental_cars)["location"])
        if menu_option == "6":
            full_map(rental_cars)