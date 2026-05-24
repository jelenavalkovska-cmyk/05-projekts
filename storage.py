import json
import sys
import os
import datetime


LIST_FILE = "expenses.json"
PRICE_FILE = "prices.json"


def load_expenses():
    """Nolasa no JSON faila. Ja fails neeksistē, atgriež tukšu sarakstu."""
    if not os.path.exists(LIST_FILE):
        return []
    try:
        with open(LIST_FILE, "r", encoding="utf-8") as f:
            return json.load(f)
    except (json.JSONDecodeError, IOError):
        return []
    
def save_expenses(expenses):
    """Saglabā sarakstu JSON failā."""
    with open(LIST_FILE, "w", encoding="utf-8") as f:
        json.dump(expenses, f, ensure_ascii=False, indent=5)


def add_expenses(FILE_PATH = LIST_FILE):
    expenses = load_expenses()
    print("--- Jaunā izdevuma pievienošana ----")

    # Atļautās izdevumu kategorijas
    CATEGORIES = ["Ēdiens", "Transports", "Izklaide", "Komunālie maksājumi", "Veselība", "Iepirkšanās", "Cits"] 

    # 1. Datuma ievade un pārbaude
    while True:
        date_input = input("Ievadiet datumu (YYYY-MM-DD): ").strip()
        try:
            # Pārbauda, vai formāts ir pareizs
            datetime.datetime.strptime(date_input, "%Y-%m-%d")
            break
        except ValueError:
            print("Kļūda: Nepareizs datuma formāts! Lūdzu, izmantojiet YYYY-MM-DD.")
    

        # 2. Summas ievade un pārbaude
    while True:
        amount_input = input("Ievadiet summu (piemēram, 15.45): ").strip()
        try:
            amount = float(amount_input)
            if amount < 0:
                print("Summa nevar būt negatīva!")
                continue
            break
        except ValueError:
            print("Kļūda: Lūdzu, ievadiet derīgu skaitli (kā decimāldaļu atdalītāju izmantojiet punktu).")

    # 3. Kategorijas izvēle
    print("\nPieejamās kategorijas:")
    for i, cat in enumerate(CATEGORIES, 1):
        print(f"{i}. {cat}")

    while True:
        try:
            cat_choice = int(
                input(f"Izvēlieties kategorijas numuru (1-{len(CATEGORIES)}): ")
            )
            if 1 <= cat_choice <= len(CATEGORIES):
                category = CATEGORIES[cat_choice - 1]
                break
            else:
                print(f"Lūdzu, izvēlieties skaitli no 1 līdz {len(CATEGORIES)}.")
        except ValueError:
            print("Kļūda: Ievadiet tikai kategorijas numuru!")


    # 4. Apraksta ievade
    descript = input("Ievadiet īsu aprakstu: ")

    # Sagatavojam jauno ierakstu
    expenses.append({"date": date_input, "amount": amount, "category": category, "description": descript})
    save_expenses(expenses)



def delete_expense(file_path = LIST_FILE):
    print("\n--- Izdevuma dzēšana ---")

    # 1. Pārbaudām, vai fails eksistē un satur datus
    if not os.path.exists(file_path) or os.path.getsize(file_path) == 0:
        print("Failā nav neviena ieraksta, ko varētu izdzēst.")
        return

    try:
        with open(file_path, "r", encoding="utf-8") as file:
            expenses_list = json.load(file)

        if not expenses_list:
            print("Izdevumu saraksts ir tukšs.")
            return

        # 2. Parādām lietotājam numurētu sarakstu, lai viņš redz, ko dzēš
        print("\nPašreizējie izdevumi:")
        print(
            f"{'Nr.':<4} | {'Datums':<12} | {'Kategorija':<20} | {'Summa':<10} | Apraksts"
        )
        print("-" * 75)

        for i, exp in enumerate(expenses_list, 1):
            date = exp.get("date", "Nezināms")
            category = exp.get("category", "Nezināma")
            amount = exp.get("amount", 0.0)
            description = exp.get("description", "")
            print(
                f"{i:<4} | {date:<12} | {category:<20} | {amount:<10.2f} | {description}"
            )

        print("-" * 75)

        # 3. Prasām lietotājam, kuru ierakstu dzēst
        while True:
            try:
                choice = int(
                    input(
                        f"Ievadiet ieraksta numuru, kuru vēlaties dzēst (1-{len(expenses_list)}): "
                    )
                )
                if 1 <= choice <= len(expenses_list):
                    # Python saraksti sākas no 0, tāpēc atņemam 1
                    index_to_delete = choice - 1
                    break
                else:
                    print(
                        f"Kļūda: Skaitlim jābūt robežās no 1 līdz {len(expenses_list)}."
                    )
            except ValueError:
                print("Kļūda: Lūdzu, ievadiet tikai veselu skaitli!")

        # 4. Izdzēšam ierakstu un parādām apstiprinājumu
        # .pop() izņem elementu no saraksta un atgriež to, lai varam parādīt, kas tika izdzēsts
        removed_expense = expenses_list.pop(index_to_delete)
        print(
            f"\nVeiksmīgi izdzēsts: {removed_expense['date']} | {removed_expense['category']} | {removed_expense['amount']} EUR"
        )

        # 5. Saglabājam atjaunoto sarakstu failā
        save_expenses(expenses_list)

        print("Izmaiņas saglabātas failā.")

    except json.JSONDecodeError:
        print("Kļūda: Fails ir bojāts un datus nevar nolasīt.")
    except Exception as e:
        print(f"Negaidīta kļūda: {e}")

