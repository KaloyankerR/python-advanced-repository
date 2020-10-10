def draw_triangle(n: int):
    for x in range(1, n + 1):
        for y in range(1, x + 1):
            print(y, end=' ')
        print()

    for x in range(n, 0, -1):
        for y in range(1, x):
            print(y, end=' ')
        print()