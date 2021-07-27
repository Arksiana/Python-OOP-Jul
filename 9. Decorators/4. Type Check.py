def type_check(type_c):
    def decorator(func):
        def wrapper(arg):
            if type_c == type(arg):
                return func(arg)
            return 'Bad Type'
        return wrapper
    return decorator


@type_check(int)
def times2(num):
    return num*2
print(times2(2))
print(times2('Not A Number'))
