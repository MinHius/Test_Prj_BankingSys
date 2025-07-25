from account import accounts_db
from logger import log_event

def run_audit():
    for name, acc in accounts_db.items():
        if acc["balance"] < 0:
            log_event(f"AUDIT: Negative balance for {name}")
        if not acc["active"]:
            log_event(f"AUDIT: Inactive account {name}")
