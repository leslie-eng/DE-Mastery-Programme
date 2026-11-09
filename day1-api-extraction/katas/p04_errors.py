class FetchError(Exception):
    pass

def to_int(value, default=None):
    # type conversion
    try:
        return int(value)
    except (TypeError, ValueError):
        return default
    
def require_positive(self, n):
    if isinstance(n, int): # check for compatibility
        if n <= 0:
            raise FetchError(f"must be positive: {n}")
        else:
            return n
    else:
        raise TypeError("please enter a number")
