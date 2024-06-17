def login():
    username = input("Wpisz login: ")
    password = input("Wpisz hasło: ")

    if username == "Natalia" and password == "geoinformatyka":  # Replace with your own credentials
        print("Zalogowano!")
    else:
        print("Błędne hasło lub login. Wpisz ponownie dane do logowania.")
        login()

login()



def read_car_rental(rental_cars: list)->None:
    print("Informacje o wypożyczalniach samochodowych: ")
    for rental_cars in rental_cars:
        print("Nazwa wypożyczalni:", rental_cars['name'])
        print("Numer telefonu:", rental_cars['number'])
        print("Ilość samochodów:", rental_cars['cars'])
        print("Liczba pracowników:", rental_cars['workers'])
        print("Współrzędne:", rental_cars['location'])

def add_car_rental(lista: list) -> None:
    name = input("Podaj nazwę firmy: ")
    number = int(input("Podaj numer telefonu: "))
    cars = int(input("Podaj liczbę samochodów: "))
    workers = int(input("Podaj liczbę pracowników: "))
    location = input("Dodaj współrzędne siedziby firmy: ")
    new_car_rental = {"name": name, "number": number, "cars": cars, "workers": workers, "location": location}
    lista.append(new_car_rental)

def remove_car_rental(rental_cars: list):
    name = input("Podaj nazwę wypożyczlni: ")
    for rental_cars in rental_cars:
        if rental_cars["name"] == name:
            rental_cars.remove(rental_cars)

def update_car_rental(rental_cars: list):
    name = input("Wprowadź nazwę wypożyczalni, którego dane chcesz zmienić: ")
    for rental_cars in rental_cars:
        if rental_cars["name"] == name:
            rental_cars["number"] = int(input("Podaj nowy numer telefonu: "))
            rental_cars["cars"] = int(input("Podaj nową liczbę samochodów: "))
            rental_cars["workers"] = int(input("Podaj nową liczbę pracowników: "))
            rental_cars["location"] = input("Podaj nowe współrzędne siedziby firmy: ")

def read_workers(workers: list)->None:
    print("Informacje o pracownikach wypożyczalni samochodowej: ")
    for workers in workers:
        print("Imię:", workers['name'])
        print("Nazwisko:", workers['surname'])
        print("Wiek:", workers['age'])
        print("Miejsce pracy:", workers['workplace'])
        print("Współrzędne miejsca pracy pracowników:", workers['location'])

def add_workers(lista: list) -> None:
    name = input("Podaj imię nowego pracownika: ")
    surname = input("Podaj nazwisko nowego pracownika: ")
    age = int(input("Podaj wiek nowego pracownika: "))
    workplace = input("Podaj nazwę firmy pracownika: ")
    location = input("Podaj współrzędne siedziby firmy, w której pracuje pracownik: ")
    new_workers = {"name": name, "surname": surname, "age": age, "workplace": workplace, "location": location}
    lista.append(new_workers)

def remove_workers(workers: list):
    surname = input("Podaj nazwisko: ")
    for workers in workers:
        if workers["surname"] == surname:
            workers.remove(workers)

def update_workers(workers: list):
    surname = input("Wprowadź nazwisko osoby, której dane chcesz zmienić: ")
    for workers in workers:
        if workers["surname"] == surname:
            workers["name"] = input("Podaj nowe imię pracownika: ")
            workers["age"] = int(input("Podaj nowy wiek pracownika: "))
            workers["workplace"] = input("Podaj nowe miejsce pracy pracownika: ")
            workers["location"] = input("Podaj nowe współrzędne siedziby firmy, w której pracuje pracownik: ")

def read_clients(clients: list)->None:
    print("Informacje o klientach wypożyczalni samochodowej: ")
    for clients in clients:
        print("Imię:", clients['name'])
        print("Nazwisko:", clients['surname'])
        print("wiek:", clients['age'])
        print("Podaj nazwę wypożyczalni samochodowej: ", clients['rental'])
        print("Współrzędne miejsca odbioru samochodu:", clients['location'])

def add_clients(lista: list) -> None:
    name = input("Podaj imię nowego klienta: ")
    surname = input("Podaj nazwisko nowego klienta: ")
    age = int(input("Podaj wiek nowego klienta: "))
    rental = input("Podaj nazwę wypożyczalni samochodowej klienta: ")
    location = input("Podaj współrzędne odbioru samochodu przez klienta: ")
    new_client = {"name": name, "surname": surname, "age": age, "rental": rental, "location": location}
    lista.append(new_client)

def remove_clients(clients: list):
    name = input("Podaj imię: ")
    for clients in clients:
        if clients["name"] == name:
            clients.remove(clients)

def update_clients(clients: list):
    surname = input("Wprowadź nazwisko osoby, której dane chcesz zmienić: ")
    for clients in clients:
        if clients["surname"] == surname:
            clients["name"] = input("Podaj nowe imię klienta: ")
            clients["age"] = int(input("Podaj nowy wiek klienta: "))
            clients["rental"] = input("Podaj nową nazwę wypożyczalni samochodowej klienta: ")
            clients["location"] = input("Podaj nowe współrzędne odbioru samochodu przez klienta: ")
