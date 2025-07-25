from balance import get_balance, update_balance
from logger import log_transaction, log_event
from account import get_account

def deposit(acc, amount):
    acc["balance"] = update_balance(acc, amount)
    log_transaction(acc)

def withdraw(acc, amount):
    if get_balance(acc) >= amount:
        acc["balance"] = update_balance(acc, -amount)
        log_transaction(acc)
    else:
        log_event(f"Withdraw failed: insufficient funds for {acc['name']}")

def transfer(sender, receiver, amount):
    if get_balance(sender) >= amount:
        update_balance(sender, -amount)
        update_balance(receiver, amount)
        log_event(f"Transferred {amount} from {sender['name']} to {receiver['name']}")
    else:
        log_event(f"Transfer failed: insufficient funds for {sender['name']}")
        
        