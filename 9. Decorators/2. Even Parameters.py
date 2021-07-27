def even_parameters(func):
    def wrapper(*args):
        if all([num % 2 == 0 if isinstance(num, int) else False for num in args]):
            return func(*args)
        return 'Please use only even numbers!'

    return wrapper


@even_parameters
def add(a, b):
    return a + b


print(add(2, 4))
print(add("Peter", 1))
