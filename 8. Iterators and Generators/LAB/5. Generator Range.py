def genrange(start, end):

    for index in range(start, end + 1):
        yield index

print(list(genrange(1, 10)))