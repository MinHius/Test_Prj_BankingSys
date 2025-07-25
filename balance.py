from account import get_account
from logger import log_event

def get_balance(acc):
    return acc["balance"]

def update_balance(acc, delta):
    acc["balance"] += delta
    log_event(f"Balance updated by {delta} for {acc['name']}")
    return acc["balance"]

def reset_balance(name):
    acc = get_account(name)
    if acc:
        acc["balance"] = 0
        log_event(f"Reset balance for {name}")