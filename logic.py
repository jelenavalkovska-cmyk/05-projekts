from datetime import datetime 


def filter_by_month(expenses, yearmonth): 

    """Atgriež izdevumus, kuru datums ir norādītajā mēnesī.""" 

    result = [] 

    for expense in expenses: 
       
       date_str = expense.get("date")
       year_month = date_str[:7]

       if year_month == yearmonth: 

        print(f"{expense['date']} | {expense['amount']:<5.2f} | {expense['category']:<15} | {expense['description']} ")
        result.append(expense) 

    return result 


def get_available_months(expenses):

    available_month = set()

    for exp in expenses:
       date_str = exp.get("date")
       year_month = date_str[:7]
       available_month.add(year_month)

    sorted_periods = sorted(list(available_month))
    
    if sorted_periods:
        for i, period in enumerate(sorted_periods, 1):
            print(f"{i}. {period}")
        print(f"Kopā atrasti {len(sorted_periods)} unikāli mēneši")
        #return(sorted_periods)
        print(f"Izvēlies, par kuru periodu Tu gribi pārskatu: 1- {len(sorted_periods)}")
    else: 
        print("Netika atrasts neviens periods")
        return None
    
    # Prasām lietotājam veikt izvēli
    while True:
            try:
                choice_period = int(input(f"\nIzvēlieties perioda numuru (1-{len(sorted_periods)}): "))
                if 1 <= choice_period <= len(sorted_periods):
                    # Atgriežam izvēlēto mēnesi kā tekstu, piemēram, "2026-05"
                    selected_month = sorted_periods[choice_period - 1]
                    #return selected_month
                    print(selected_month)
                    print(f"\n--- Izdevumi par periodu: {selected_month} ---")
                    filter_by_month(expenses, selected_month) 
                    break
                else:
                    print(f"Lūdzu, ievadiet skaitli no 1 līdz {len(sorted_periods)}.")
                    break
            except ValueError:
                print("Kļūda: Lūdzu, ievadiet tikai numuru!")          


                   

 





def sum_by_category(expenses): 

    """Atgriež vārdnīcu: {kategorija: summa}.""" 

    totals = {} 

    for expense in expenses: 

        cat = expense["category"] 

        totals[cat] = totals.get(cat, 0) + expense["amount"] 

    return {cat: round(total, 2) for cat, total in totals.items()} 


def sum_total(expenses): 

    """Atgriež vārdnīcu: {kategorija: summa}.""" 

    totals = 0

    for expense in expenses: 

        totals += expense["amount"] 

    return totals 