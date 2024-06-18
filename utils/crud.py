def login():
    username = input("Wpisz login: ")
    password = input("Wpisz hasło: ")

    # if username == "Natalia" and password == "geoinformatyka":  # Replace with your own credentials
    if username == "a" and password == "a":  # Replace with your own credentials
        print("Zalogowano!")
    else:
        print("Błędne hasło lub login. Wpisz ponownie dane do logowania.")
        login()


def read_car_rental(rental_cars: list) -> None:
    print("Informacje o wypożyczalniach samochodowych: ")
    for rental_cars in rental_cars:
        print("Nazwa wypożyczalni:", rental_cars['name'])
        print("Numer telefonu:", rental_cars['number'])
        print("Ilość samochodów:", rental_cars['cars'])
        print("Współrzędne:", rental_cars['location'])


def add_car_rental(lista: list) -> None:
    name = input("Podaj nazwę firmy: ")
    number = int(input("Podaj numer telefonu: "))
    cars = int(input("Podaj liczbę samochodów: "))
    location = read_coordinates("Dodaj współrzędne siedziby firmy: ")
    new_car_rental = {"name": name, "number": number, "cars": cars, "location": location}
    lista.append(new_car_rental)


def remove_car_rental(rental_cars: list, clients: list, workers: list):
    name = read_rental_name("Podaj nazwę wypożyczalni: ", rental_cars)
    for i, rental_place in enumerate(rental_cars):
        if rental_place["name"] == name:
            rental_cars.pop(i)
            print("Usunięto wypożyczalnie wraz z jej klientami i pracownikami", rental_place["name"])
            new_workers = [worker for worker in workers if worker["workplace"] != name]
            new_clients = [client for client in clients if client["rental"] != name]
            workers[:] = new_workers
            clients[:] = new_clients
            break


def update_car_rental(rental_cars: list):
    name = read_rental_name("Wprowadź nazwę wypożyczalni, którego dane chcesz zmienić: ", rental_cars)
    for rental_cars in rental_cars:
        if rental_cars["name"] == name:
            rental_cars["number"] = int(input("Podaj nowy numer telefonu: "))
            rental_cars["cars"] = int(input("Podaj nową liczbę samochodów: "))
            rental_cars["location"] = input("Podaj nowe współrzędne siedziby firmy: ")


def read_workers(workers: list) -> None:
    rental_name = input("Podaj nazwę wypożyczalni (brak firmy oznacza wszystkie): ")
    print("Informacje o pracownikach wypożyczalni samochodowej: ")
    for worker in workers:
        if worker['workplace'] != rental_name and rental_name != "":
            continue
        print("Imię:", worker['name'])
        print("Nazwisko:", worker['surname'])
        print("Wiek:", worker['age'])
        print("Miejsce pracy:", worker['workplace'])
        print("Współrzędne miejsca pracy pracowników:", worker['location'])


def read_rental_name(message: str, rental_cars: list) -> str:
    rental_name = input(message)
    selected_rental = None
    for rental_candidate in rental_cars:
        if rental_candidate["name"] == rental_name:
            selected_rental = rental_candidate
            break
    if selected_rental is None:
        print("Wybrana firma nie istnieje. Wybierz jedną z listy:")
        for rental_candidate in rental_cars:
            print(rental_candidate["name"])
        return read_rental_name(message, rental_cars)
    else:
        return rental_name


def read_coordinates(message: str) -> dict:
    coordinates = input(message)
    latitude, longitude = coordinates.split(",")
    return {"latitude": float(latitude), "longitude": float(longitude)}


def add_workers(workers: list, rental_cars: list) -> None:
    name = input("Podaj imię nowego pracownika: ")
    surname = input("Podaj nazwisko nowego pracownika: ")
    age = int(input("Podaj wiek nowego pracownika: "))
    workplace = read_rental_name("Podaj nazwę miejsca pracy pracownika: ", rental_cars)
    location = read_coordinates("Podaj współrzędne miejsca zamieszkania pracownika: ")

    new_workers = {"name": name, "surname": surname, "age": age, "workplace": workplace, "location": location}
    workers.append(new_workers)


def remove_workers(workers: list):
    surname = input("Podaj nazwisko: ")
    for i, worker in enumerate(workers):
        if worker["surname"] == surname:
            workers.pop(i)
            print("Usunięto pracownika", worker["name"], worker["surname"])
            break


def update_workers(workers: list):
    surname = input("Wprowadź nazwisko osoby, której dane chcesz zmienić: ")
    for workers in workers:
        if workers["surname"] == surname:
            workers["name"] = input("Podaj nowe imię pracownika: ")
            workers["age"] = int(input("Podaj nowy wiek pracownika: "))
            workers["workplace"] = input("Podaj nowe miejsce pracy pracownika: ")
            workers["location"] = read_coordinates("Podaj współrzędne miejsca zamieszkania pracownika: ")


def read_clients(clients: list) -> None:
    rental_name = input("Podaj nazwę wypożyczalni (brak firmy oznacza wszystkie): ")
    print("Informacje o klientach wypożyczalni samochodowej: ")
    for client in clients:
        if client['rental'] != rental_name and rental_name != "":
            continue
        print("Imię:", client['name'])
        print("Nazwisko:", client['surname'])
        print("Wiek:", client['age'])
        print("Wypożyczalnia samochodowa:", client['rental'])
        print("Współrzędne miejsca odbioru samochodu:", client['location'])


def add_clients(clients: list, rental_cars: list) -> None:
    name = input("Podaj imię nowego klienta: ")
    surname = input("Podaj nazwisko nowego klienta: ")
    age = int(input("Podaj wiek nowego klienta: "))
    rental = read_rental_name("Podaj nazwę wypożyczalni samochodowej klienta: ", rental_cars)
    location = read_coordinates("Podaj współrzędne odbioru samochodu przez klienta: ")
    new_client = {"name": name, "surname": surname, "age": age, "rental": rental, "location": location}
    clients.append(new_client)


def remove_clients(clients: list):
    surname = input("Podaj nazwisko: ")
    for i, client in enumerate(clients):
        if client["surname"] == surname:
            clients.pop(i)
            print("Usunięto klienta", client["name"], client["surname"])
            break


def update_clients(clients: list, rental_cars: list):
    surname = input("Wprowadź nazwisko osoby, której dane chcesz zmienić: ")
    for clients in clients:
        if clients["surname"] == surname:
            clients["name"] = input("Podaj nowe imię klienta: ")
            clients["age"] = int(input("Podaj nowy wiek klienta: "))
            clients["rental"] = read_rental_name("Podaj nową nazwę wypożyczalni samochodowej klienta: ", rental_cars)
            clients["location"] = read_coordinates("Podaj nowe współrzędne odbioru samochodu przez klienta: ")
