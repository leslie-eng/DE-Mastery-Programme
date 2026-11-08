class FetchError(Exception):
    def to_int(self, value, default=None):
        # type conversion
        try:
            if int(value):
                return int(value)
            else:
                return default
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
