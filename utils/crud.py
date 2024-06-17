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
        #print("Adress:", rental_cars['location'])
        print("Liczba pracowników:", rental_cars['workers'])
        #print("Klienci:", rental_cars['clients'])

def add_car_rental(lista: list) -> None:
    name = input("Podaj nazwę firmy: ")
    number = int(input("Podaj numer telefonu: "))
    cars = int(input("Podaj liczbę samochodów: "))
    workers = int(input("Podaj liczbę pracowników: "))
    #location = input("Podaj nazwę miejscowości siedziby firmy: ")
    new_car_rental = {"name": name, "number": number, "cars": cars, "workers": workers}
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
            #rental_cars["location"] = input("Podaj nową lokalizację siedziby firmy: ")

def read_workers(workers: list)->None:
    workplace = input("Wprowadź nazwę wypożyczalni, którego listę pracowników chcesz zobaczyć: ")
    for workers in workers:
        if workers["workplace"] == workplace:
            print("Imię:", workers['name'])
            print("Nazwisko:", workers['surname'])
            print("wiek:", workers['age'])

def add_workers(lista: list) -> None:
    workplace = input("Wprowadź nazwę wypożyczalni, do której chcesz dodać pracownika: ")
    for workers in workers:
        if workers["workplace"] == workplace:
            name = input("Podaj imię nowego pracownika: ")
            surname = input("Podaj nazwisko nowego pracownika: ")
            age = int(input("Podaj wiek nowego pracownika: "))
            #location = input("Podaj nazwę miejscowości siedziby firmy: ")
            workplace = input("Podaj miejsce pracy pracownika: ")
            new_workers = {"name": name, "surname": surname, "age": age, "workplace": workplace}
            lista.append(new_workers)

def remove_workers(workers: list):
    name = input("Podaj imię: ")
    for workers in workers:
        if workers["name"] == name:
            workers.remove(workers)

def update_workers(workers: list):
    workplace = input("Wprowadź nazwę wypożyczalni, którego listę pracowników chcesz zaktualizować: ")
    for workers in workers:
        if workers["workplace"] == workplace:
            name = input("Wprowadź imię osoby, której dane chcesz zmienić: ")
    for workers in workers:
        if workers["name"] == name:
            workers["surname"] = input("Podaj nowe nazwisko pracownika: ")
            workers["age"] = int(input("Podaj nowy wiek pracownika: "))
            workers["workplace"] = input("Podaj nowe miejsce pracy pracownika: ")
            #rental_cars["location"] = input("Podaj nową lokalizację siedziby firmy: ")

def read_clients(clients: list)->None:
    rental = input("Wprowadź nazwę wypożyczalni, którego listę klientów chcesz klienta: ")
    for clients in clients:
        if clients["rental"] == rental:
            print("Imię:", rental['name'])
            print("Nazwisko:", rental['surname'])
            print("wiek:", rental['age'])

def add_clients(lista: list) -> None:
    rental = input("Wprowadź nazwę wypożyczalni, do której chcesz dodać klienta: ")
    for clients in clients:
        if clients["rental"] == rental:
            name = input("Podaj imię nowego klienta: ")
            surname = input("Podaj nazwisko nowego klienta: ")
            age = int(input("Podaj wiek nowego klienta: "))
            #location = input("Podaj nazwę miejscowości siedziby firmy: ")
            rental = input("Podaj miejsce pracy klienta: ")
            new_workers = {"name": name, "surname": surname, "age": age, "rental": rental}
            lista.append(new_rental)

def remove_clients(clients: list):
    name = input("Podaj imię: ")
    for clients in clients:
        if clients["name"] == name:
            clients.remove(clients)

def update_clients(clients: list):
    rental = input("Wprowadź nazwę wypożyczalni, którego listę klientów chcesz zaktualizować: ")
    for clients in clients:
        if clients["rental"] == rental:
            name = input("Wprowadź imię osoby, której dane chcesz zmienić: ")
    for clients in clients:
        if clients["name"] == name:
            clients["surname"] = input("Podaj nowe nazwisko klienta: ")
            clients["age"] = int(input("Podaj nowy wiek klienta: "))
            clients["rental"] = input("Podaj nowe miejsce pracy klienta: ")
            #rental_cars["location"] = input("Podaj nową lokalizację siedziby firmy: ")


# def add_car_rental(lista: list) -> None:
#     name = input("Podaj nazwę firmy: ")
#     number = int(input("Podaj numer telefonu firmy"))
#     cars = int(input("Podaj liczbę samochodów: "))
#     location = input("Podaj współrzędne siedziby firmy: ")
#     new_car_rental = {"name": name, "number": number, "cars": cars, 'location': location }
#     lista.append(new_car_rental)
#     workers = []
#         name = input("Podaj imię pracownika: ")
#         surname = input("Podaj nazwisko pracownika: ")
#         age = int(input("Podaj wiek pracownika: "))
#         location = input("Podaj współrzędne miejsca pracy pracownika: ")
#         workers.append({"name": name, "surname": surname, "age": age, "location": location})
#     clients = []
#     name = input("Podaj imię klienta: ")
#     surname = input("Podaj nazwisko klienta: ")
#     age = int(input("Podaj wiek klienta: "))
#     location = input("Podaj współrzędne miejsca odbioru samochodu przez klienta: ")
#     cients.append({"name": name, "surname": surname, "age": age, "location": location})
#
# def remove_car_rental(rental_cars: list):
#     name = input("Podaj nazwę: ")
#     for rental_cars in rental_cars:
#         if rental_cars["name"] == name:
#             rental_cars.remove(rental_cars)
#
# def update_car_rental(rental_cars: list):
#     name = input("Wprowadź nazwę wypożyczalni, którego dane chcesz zmienić: ")
#     for rental_cars in rental_cars:
#         if rental_cars["name"] == name:
#             rental_cars["cars"] = input("Podaj nową liczbę samochodów: ")
#             rental_cars["workers"] = input("Podaj nową liczbę pracowników: ")
#             rental_cars["location"] = input("Podaj nową lokalizację siedziby firmy: ")
#             print("Edycja danych pracowników:")
#             for workers in rental_cars['workers']:
#                 workers['name'] = input(f"Podaj nowe imię pracownika {workers['name']}: ")
#                 workers['surname'] = input(f"Podaj nowe nazwisko pracownika {workers['surname']} : ")
#             print("Edycja danych klientów:")
#             for clients in rental_cars['clients']:
#                 clients['name'] = input(f"Podaj nowe imię klienta: {client['name']}
#                 clients['surname'] = input(f"Podaj nowe nazwisko klienta: {client['last_name']}
#                 clients['age'] = input(f"Podaj wiek klienta: {client['age']}
#                 clients['location'] = input(f"Podaj nowe współrzędne klienta {customer['name']}
#             print("Dane wypożyczalni samochodowej zostały zaktualizowane.")