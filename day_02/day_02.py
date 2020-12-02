def get_input():
    with open('./input.txt') as f:
        pws = f.readlines()
    return pws


def parse(line):
    split = line.split()
    limits = split[0].split('-')
    low = int(limits[0])
    high = int(limits[1])
    letter = split[1][0]
    pw = split[2]
    return {"low": low, "high": high, "letter": letter, "pw": pw}


def validate(line):
    count = 0
    for char in line['pw']:
        if char == line['letter']:
            count += 1

    if line["low"] <= count <= line["high"]:
        return True

    return False


def part1():
    pws = get_input()
    count = 0
    for line in pws:
        if validate(parse(line)):
            count += 1
    print("Part 1 - {} valid passwords".format(count))


def part2_parse(line):
    split = line.split()
    limits = split[0].split('-')
    index1 = int(limits[0])
    index2 = int(limits[1])
    letter = split[1][0]
    pw = split[2]
    return {"index1": index1, "index2": index2, "letter": letter, "pw": pw}


def part2_validate(line):
    count = 0
    if bool(line['pw'][line["index1"] - 1] == line['letter']) ^ bool(
        line['pw'][line["index2"] - 1] == line['letter']
    ):
        return True

    return False


def part2():
    pws = get_input()
    count = 0
    for line in pws:
        if part2_validate(part2_parse(line)):
            count += 1
    print("Part 2 - {} valid passwords".format(count))


if __name__ == '__main__':
    part1()
    part2()
