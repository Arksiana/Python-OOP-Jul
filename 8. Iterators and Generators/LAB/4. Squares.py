def squares(n):

    for index in range(1, n + 1):
        result = index ** 2
        yield result



print(list(squares(5)))