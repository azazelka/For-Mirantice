def cycle_decorator(count):
    def my_decorator(fn):
        def _wrapped(*args):
            for i in range(count):
                fn(*args)
        return _wrapped
    return my_decorator

