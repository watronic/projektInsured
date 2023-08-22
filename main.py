import csv

# Vytvoření databáze pojištěných osob
insured_people = []

# Funkce pro vytvoření nového pojištěného
def create_insured_person():
    name = input("Zadejte jméno: ")
    last_name = input("Zadejte příjmení: ")
    age = int(input("Zadejte věk: "))
    phone_number = input("Zadejte telefonní číslo: ")

    insured_person = {
        "name": name,
        "last_name": last_name,
        "age": age,
        "phone_number": phone_number
    }

    insured_people.append(insured_person)

# Funkce pro zobrazení seznamu všech pojištěných
def list_insured_people():
    for insured_person in insured_people:
        print(insured_person)


# Funkce pro vyhledání pojištěného podle jména a příjmení
def find_insured_person(name, last_name):
    for insured_person in insured_people:
        if insured_person["name"] == name and insured_person["last_name"] == last_name:
            return insured_person

    return None

# Funkce pro uložení databáze pojištěných do CSV souboru
def save_insured_people_to_csv():
    with open("insured_people.csv", "w", newline="") as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(["name", "last_name", "age", "phone_number"])
        for insured_person in insured_people:
            writer.writerow([insured_person["name"], insured_person["last_name"], insured_person["age"], insured_person["phone_number"]])

# Hlavní menu
while True:
    print("1. Vytvořit nového pojištěného")
    print("2. Zobrazit seznam všech pojištěných")
    print("3. Najít pojištěného")
    print("4. Uložit databázi pojištěných do CSV souboru")
    print("5. Konec")

    choice = int(input("Zvolte možnost: "))

    if choice == 1:
        create_insured_person()
        save_insured_people_to_csv()
    elif choice == 2:
        list_insured_people()
    elif choice == 3:
        name = input("Zadejte jméno: ")
        last_name = input("Zadejte příjmení: ")
        insured_person = find_insured_person(name, last_name)
        if insured_person is not None:
            print(insured_person)
        else:
            print("Pojištěný nebyl nalezen.")
    elif choice == 4:
        save_insured_people_to_csv()
    elif choice == 5:
        break
