from utils.formatter import format_account
from utils.timestamp import timestamp

log_file = []

def log_transaction(acc):
    msg = f"[{timestamp()}] Transaction on {format_account(acc)}"
    log_file.append(msg)
    print(msg)

def log_creation(acc):
    msg = f"[{timestamp()}] Created account for {format_account(acc)}"
    log_file.append(msg)
    print(msg)

def log_event(msg):
    full = f"[{timestamp()}] EVENT: {msg}"
    log_file.append(full)
    print(full)