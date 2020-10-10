def create(count: int):
    if count == 1:
        return [0]
    elif count == 2:
        return [0, 1]
    else:
        x = create(count - 1)
        x.append(sum(x[:-3:-1]))
        return x


def locate(number: int, sequence: list):
    return [x for x in range(len(sequence)) if sequence[x] == number]
