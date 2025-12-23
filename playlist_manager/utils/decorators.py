import functools
from datetime import datetime

def log_action(func):
    """
    Decorator to log function execution with timestamp.
    Usage: @log_action
    """
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        print(f"[{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}] Executing {func.__name__}...")
        result = func(*args, **kwargs)
        print(f"[{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}] Finished {func.__name__}.")
        return result
    return wrapper
