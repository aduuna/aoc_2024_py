from functools import partial, cmp_to_key


def read_data(file="input.txt"):
    with open(file) as f:
        data = f.readlines()
    # basic clean up here
    data = [x.strip() for x in data]

    rules = []
    updates = []
    on_rules = False
    for line in data:
        if line == "":
            on_rules = True
            continue
        if line and not on_rules:
            rules.append(line.split("|"))
        else:
            updates.append(line.split(","))

    rule_map = {}
    for k, v in rules:
        if rule_map.get(k):
            rule_map[k].append(v)
        else:
            rule_map[k] = [v]

    data = {'rules': rule_map, 'updates': updates}

    return data


def check_ordering_validity(update, rules):
    is_valid = True
    for i in range(len(update)-1):
        page_number = update[i]
        rule = rules.get(page_number) or []
        numbers_to_the_right_are_valid = [(x in rule) for x in update[i + 1:]]
        if not all(numbers_to_the_right_are_valid):
            is_valid = False
            break
    return is_valid


def sum_mid_points(valid_updates):
    result = 0
    for update in valid_updates:
        mid_point = len(update) // 2
        result += int(update[mid_point])

    return result

def part_1(data):
    valid_updates = []
    rules = data["rules"]
    for update in data["updates"]:
        valid = check_ordering_validity(update, rules)
        if valid:
            valid_updates.append(update)

    return sum_mid_points(valid_updates)


def sorting_key(a, b, rules=None):
    if rule := rules.get(a):
        if b in rule:
            return 1
        else:
            return -1
    return -1

def reorder(update, rules):
    key = cmp_to_key(partial(sorting_key, rules=rules))
    res = sorted(update, key=key)
    return res

def part_2(data):
    invalid_updates = []
    rules = data["rules"]
    for update in data["updates"]:
        valid = check_ordering_validity(update, rules)
        if not valid:
            invalid_updates.append(update)
    print("invalid")
    print(invalid_updates)
    
    reordered_invalid_updates = []
    for update in invalid_updates:
        reordered_invalid_updates.append(reorder(update, rules))

    print(reordered_invalid_updates)
    return sum_mid_points(reordered_invalid_updates)


if __name__ == '__main__':

    part_1 = part_1(read_data())
    print("Part 1 answer =>", part_1)

    part_2 = part_2(read_data())
    print("Part 2 answer =>", part_2)