from storage import load_expenses, save_expenses, add_expenses, delete_expense

from logic import sum_total, filter_by_month, sum_by_category 

from logic import get_available_months

from export import export_to_csv 

from datetime import date 

 

CATEGORIES = ["Ēdiens", "Transports", "Izklaide", "Komunālie maksājumi", "Veselība", "Iepirkšanās", "Cits"] 

 

def show_menu(): 

    """Parāda galveno izvēlni un atgriež lietotāja izvēli.""" 

    print("1) Pievienot izdevumu") 

    print("2) Parādīt izdevumus") 

    print("3) Filtrēt pēc mēneša")

    print("4) Kopsumma pa kategorijām")

    print("5) Dzēst izdevumu")

    print("6) Eksportēt CSV")

    print("7) Iziet no programmas") 

    return input("\nIzvēlies darbību (1-7): ") 

 

def main(): 

    """Galvenā programmas cilpa/cikls.""" 

    expenses = load_expenses() 

    while True: 

        choice = show_menu() 

        if choice == "1": 

            add_expenses() 
            

        elif choice == "2": 
            print("--- Izdevumu saraksts ---")

            print(f"Datums      Apjoms  Kategorija        Apraksts")

            for item in expenses:
               
               print(f"{item['date']} | {item['amount']:<5.2f} | {item['category']:<15} | {item['description']} ")

            return(expenses) 
        

        elif choice == "3":
            print("\n --- Notiek filtrēšana --- ")
            get_available_months(expenses)
            
            break

        elif choice == "5":
            delete_expense()
            

        elif choice == "7": 

            print("Uz redzēšanos!") 

            break 

 

if __name__ == "__main__": 

    main() 