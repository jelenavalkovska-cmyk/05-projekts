from storage import load_expenses, save_expenses, add_expenses

from logic import sum_total, filter_by_month, sum_by_category 

#from logic import get_available_months 

from export import export_to_csv 

from datetime import date 

 

CATEGORIES = ["Ēdiens", "Transports", "Izklaide", "Komunālie maksājumi", "Veselība", "Iepirkšanās", "Cits"] 

 

def show_menu(): 

    """Parāda galveno izvēlni un atgriež lietotāja izvēli.""" 

    print("\n1) Pievienot izdevumu") 

    print("2) Parādīt izdevumus") 

    print("7) Iziet no programmas") 

    # ... pārējās komandas ... 

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
            

        elif choice == "7": 

            print("Uz redzēšanos!") 

            break 

 

if __name__ == "__main__": 

    main() 