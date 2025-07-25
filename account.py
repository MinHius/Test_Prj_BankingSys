from logger import log_creation, log_event
from balance import update_balance
from security import validate_name

accounts_db = {}

def create_account(name):
    if not validate_name(name):
        log_event("Invalid account name")
        return None
    acc = {"name": name, "balance": 0, "active": True}
    accounts_db[name] = acc
    log_creation(acc)
    return acc

def deactivate_account(name):
    if name in accounts_db:
        accounts_db[name]["active"] = False
        log_event(f"Deactivated {name}")

def get_account(name):
    return accounts_db.get(name)