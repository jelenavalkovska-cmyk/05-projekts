from datetime import datetime 

 

def filter_by_month(expenses, year, month): 

    """Atgriež izdevumus, kuru datums ir norādītajā mēnesī.""" 

    result = [] 

    for expense in expenses: 

        d = datetime.strptime(expense["date"], "%Y-%m-%d") 

        if d.year == year and d.month == month: 

            result.append(expense) 

    return result 

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