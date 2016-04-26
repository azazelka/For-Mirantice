def cycle_decorator(fn):
    def _wrapped(*args):
        for i in range(5000):
            fn(*args)
    return _wrapped
