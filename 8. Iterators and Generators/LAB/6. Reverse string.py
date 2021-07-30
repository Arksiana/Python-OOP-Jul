def reverse_text(param):
    yield param[::-1]


for char in reverse_text("step"):
    print(char, end='')