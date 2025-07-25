from account import create_account, deactivate_account
from transactions import deposit, withdraw, transfer
from logger import log_transaction
from audit import run_audit


def main():
    alice = create_account("Alice")
    bob = create_account("Bob")
    deposit(alice, 500)
    withdraw(alice, 200)
    transfer(alice, bob, 100)
    deactivate_account("Bob")
    run_audit()
    log_transaction(alice)

if __name__ == "__main__":
    main()