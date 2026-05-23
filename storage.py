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