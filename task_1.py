def logger(f):
    def wrapper(*args, **kwargs):
        print(f"{f.__name__} called with {args}")
        return
    return wrapper


@logger
def add(x, y):
    return x + y


@logger
def square_all(*args):
    return [arg ** 2 for arg in args]


print(add(4, 5))