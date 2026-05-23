import json
import sys
import os


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