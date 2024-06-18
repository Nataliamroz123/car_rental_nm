from models.data_source import rental_cars, workers, clients
from utils.crud import read_car_rental, add_car_rental, remove_car_rental, update_car_rental, read_workers, add_workers, \
    remove_workers, update_workers, read_clients, add_clients, remove_clients, update_clients, login
from utils.emap import all_rentals_map, workers_map, clients_map


# Definicja menu głównego
def main_menu():
    print("Menu główne:")
    print("0. Wyjście")
    print("1. Wypożyczalnie samochodowe")
    print("2. Pracownicy wypożyczalni samochodowych")
    print("3. Klienci wypożyczalni samochodowych")
    choice = input("Wybierz opcję: ")
    return choice


# Definicja menu podręcznego
def sub_menu(title):
    print(f"Menu {title}:")
    print("1. Wyświetl")
    print("2. Dodaj")
    print("3. Usuń")
    print("4. Aktualizuj")
    print("5. Mapa")
    choice = input("Wybierz opcję: ")
    return choice



login()

while True:
    choice = main_menu()
    if choice == "0":
        break
    if choice == "1":
        sub_choice = sub_menu("Wypożyczalnie samochodowe")
        if sub_choice == "1":
            read_car_rental(rental_cars)
        elif sub_choice == "2":
            add_car_rental(rental_cars)
        elif sub_choice == "3":
            remove_car_rental(rental_cars, clients, workers)
        elif sub_choice == "4":
            update_car_rental(rental_cars)
        elif sub_choice == "5":
            all_rentals_map(rental_cars)
    elif choice == "2":
        sub_choice = sub_menu("Pracownicy wypożyczalni samochodowych")
        if sub_choice == "1":
            read_workers(workers)
        elif sub_choice == "2":
            add_workers(workers, rental_cars)
        elif sub_choice == "3":
            remove_workers(workers)
        elif sub_choice == "4":
            update_workers(workers)
        elif sub_choice == "5":
            workers_map(workers)
    elif choice == "3":
        sub_choice = sub_menu("Klienci wypożyczalni samochodowych")
        if sub_choice == "1":
            read_clients(clients)
        elif sub_choice == "2":
            add_clients(clients)
        elif sub_choice == "3":
            remove_clients(clients)
        elif sub_choice == "4":
            update_clients(clients, rental_cars)
        elif sub_choice == "5":
            clients_map(clients)
    else:
        print("Nieprawidłowy wybór. Spróbuj ponownie.")
