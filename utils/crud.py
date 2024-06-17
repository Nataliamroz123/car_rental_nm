def read_car_rental(rental_cars: list)->None:
    print("Informacje o wypożyczalniach samochodowych: ")
    for rental_cars in rental_cars:
        print("Nazwa wypożyczalni:", rental_cars['name'])
        print("Numer telefonu:", rental_cars['number'])
        print("Ilość samochodów:", rental_cars['cars'])
        print("Adress:", rental_cars['location'])
        print("Pracownicy:", rental_cars['workers'])
        print("Klienci:", rental_cars['clients'])


def add_car_rental(lista: list) -> None:
    name = input("Podaj nazwę firmy: ")
    number = int(input("Podaj numer telefonu firmy"))
    cars = int(input("Podaj liczbę samochodów: "))
    location = input("Podaj współrzędne siedziby firmy: ")
    new_car_rental = {"name": name, "number": number, "cars": cars, 'location': location }
    lista.append(new_car_rental)
    workers = []
        name = input("Podaj imię pracownika: ")
        surname = input("Podaj nazwisko pracownika: ")
        age = int(input("Podaj wiek pracownika: "))
        location = input("Podaj współrzędne miejsca pracy pracownika: ")
        workers.append({"name": name, "surname": surname, "age": age, "location": location})
    clients = []
    name = input("Podaj imię klienta: ")
    surname = input("Podaj nazwisko klienta: ")
    age = int(input("Podaj wiek klienta: "))
    location = input("Podaj współrzędne miejsca odbioru samochodu przez klienta: ")
    cients.append({"name": name, "surname": surname, "age": age, "location": location})

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
            print("Edycja danych pracowników:")
            for workers in rental_cars['workers']:
                workers['name'] = input(f"Podaj nowe imię pracownika {workers['name']}: ")
                workers['surname'] = input(f"Podaj nowe nazwisko pracownika {workers['surname']} : ")
            print("Edycja danych klientów:")
            for clients in rental_cars['clients']:
                clients['name'] = input(f"Podaj nowe imię klienta: {client['name']}
                clients['surname'] = input(f"Podaj nowe nazwisko klienta: {client['last_name']}
                clients['age'] = input(f"Podaj wiek klienta: {client['age']}
                clients['location'] = input(f"Podaj nowe współrzędne klienta {customer['name']}
            print("Dane wypożyczalni samochodowej zostały zaktualizowane.")
def login():
    username = input("Wpisz login: ")
    password = input("Wpisz hasło: ")

    if username == "Natalia" and password == "geoinformatyka":  # Replace with your own credentials
        print("Zalogowano!")
    else:
        print("Błędne hasło lub login. Wpisz ponownie dane do logowania.")
        login()

login()