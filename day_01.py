def parse():
    with open('day_01.txt', 'r') as input:
        list_one = []
        list_two = []

        for line in input:
            lsplit = line.split()
            num_one = int(lsplit[0])
            num_two = int(lsplit[-1])
            list_one.append(num_one)
            list_two.append(num_two)
    return [list_one, list_two]


def silver(list_one, list_two):
    list_one.sort()
    list_two.sort()

    offsets = 0

    for num_one, num_two in zip(list_one, list_two):
        offsets += abs(num_one - num_two)

    return offsets


def gold(list_one, list_two):
    list_one.sort()
    list_two.sort()

    list_two_freq = {}

    for num in list_two:
        list_two_freq[num] = list_two_freq.get(num, 0) + 1

    similarity_scores = 0

    for num in list_one:
        similarity_scores += list_two_freq.get(num, 0) * num

    return similarity_scores


if __name__ == "__main__":
    list_one, list_two = parse()
    print("silver: ", silver(list_one, list_two))
    print("gold: ", gold(list_one, list_two))
