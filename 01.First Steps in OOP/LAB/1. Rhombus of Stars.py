def draw_line(count, symbol, offset_count=0):
    offset = offset_count * " "
    content = (f"{symbol} " * count).strip()
    print(f"{offset}{content}")


def draw_rhombus(n):
    for i in range(n):
        draw_line(i + 1, "*", n - i - 1, )

    for i in range(n - 2, -1, - 1):
        draw_line(i + 1, "*", n - i - 1, )


n = int(input())
draw_rhombus(n)