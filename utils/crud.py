def read_car_rental(rental_cars: list)->None:
    print("Informacje o wypożyczalniach samochodowych: ")
    for rental_cars in rental_cars:
        print(f'\tWypożyczalnia samochodowa {rental_cars["name"]} ma {rental_cars["cars"]} samochodów i pracuje w niej {rental_cars["workers"]} pracowników.')
def add_car_rental(lista: list) -> None:
    name = input("Podaj nazwę firmy: ")
    cars = int(input("Podaj liczbę samochodów: "))
    workers = int(input("Podaj liczbę pracowników: "))
    location = input("Podaj nazwę miejscowości siedziby firmy: ")
    new_car_rental = {"name": name, "cars": cars, "workers": workers, 'location': location }
    lista.append(new_car_rental)

def remove_car_rental(rental_cars: list):
    name = input("Podaj nazwę: ")
    for rental_cars in rental_cars:
        if rental_cars["name"] == name:
            rental_cars.remove(rental_cars)

def update_car_rental(rental_cars: list):
    name = input("Wprowadź nazwę wypożyczalni, którego dane chcesz zmienić: ")
    for rental_cars in rental_cars:
        if rental_cars["name"] == name:
            rental_cars["cars"] = input("Podaj nową liczbę samochodów: ")
            rental_cars["workers"] = input("Podaj nową liczbę pracowników: ")
            rental_cars["location"] = input("Podaj nową lokalizację siedziby firmy: ")
def login():
    username = input("Enter your username: ")
    password = input("Enter your password: ")

    if username == "Natalia" and password == "geoinformatyka":  # Replace with your own credentials
        print("Login successful!")
    else:
        print("Invalid credentials. Try again!")
        login()

login()