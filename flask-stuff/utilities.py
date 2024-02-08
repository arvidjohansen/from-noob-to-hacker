# utilities.py
from datetime import datetime

def time_since(date):
    # first check if the date is a string
    if isinstance(date, str):
        return ""

    now = datetime.utcnow()
    diff = now - date

    if diff.days > 0:
        return f'{diff.days} days ago'
    elif diff.seconds > 3600:
        return f'{diff.seconds // 3600} hours ago'
    elif diff.seconds > 60:
        return f'{diff.seconds // 60} minutes ago'
    else:
        return 'just now'

def default_if_none(val, default_val):
    if val is None:
        return default_val
    return val