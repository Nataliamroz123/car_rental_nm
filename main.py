from models.data_source import rental_cars, workers, clients
from utils.crud import read_car_rental, add_car_rental, remove_car_rental, update_car_rental, read_workers, add_workers, \
    remove_workers, update_workers, read_clients, add_clients, remove_clients, update_clients
#from utils.emap import single_map


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
    choice = input("Wybierz opcję: ")
    return choice


# Główna pętla programu
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
            remove_car_rental(rental_cars)
        elif sub_choice == "4":
            update_car_rental(rental_cars)
    elif choice == "2":
        sub_choice = sub_menu("Pracownicy")
        if sub_choice == "1":
            read_workers(workers)
        elif sub_choice == "2":
            add_workers(workers)
        elif sub_choice == "3":
            remove_workers(workers)
        elif sub_choice == "4":
            update_workers(workers)
    elif choice == "3":
        sub_choice = sub_menu("Klienci")
        if sub_choice == "1":
            read_clients(clients)
        elif sub_choice == "2":
            add_clients(clients)
        elif sub_choice == "3":
            remove_clients(clients)
        elif sub_choice == "4":
            update_clients(clients)
    else:
        print("Nieprawidłowy wybór. Spróbuj ponownie.")
