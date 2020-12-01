def get_input():
    with open('./input.txt') as f:
        expenses = [int(x) for x in f.readlines()]
    return expenses


def process_two(target=2020, expenses=get_input()):
    while len(expenses) > 1:
        head = expenses[0]
        expenses = expenses[1:]
        for item in expenses:
            if head + item == target:
                return [head, item]
    return None


def process_three():
    expenses = get_input()
    val = None
    while len(expenses) > 1 and not val:
        head = expenses[0]
        expenses = expenses[1:]
        val = process_two(target=2020 - head, expenses=expenses)

    if val:
        return [head] + val


if __name__ == '__main__':
    out = process_two()
    print("Part 1 --> {} * {} = {}".format(out[0], out[1], out[0] * out[1]))
    out = process_three()
    print("Part 2 --> {} * {} * {} = {}".format(out[0], out[1], out[2], out[0] * out[1] * out[2]))
