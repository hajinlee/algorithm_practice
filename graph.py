def num_connected_groups(num_computers, edges):
    parents = [-1] * num_computers

    # helper function that links computers A and B
    def merge(a, b):
        # find a's parent
        # find b's parent
        # set a's parent to b's parent
        while parents[a] != -1:
            a = parents[a]

        while parents[b] != -1:
            b = parents[b]

        if a != b:
            parents[a] = b

    for edge in edges:
        merge(edge[0], edge[1])

    count = 0

    for x in parents:
        if x == -1:
            count += 1

    # count number of -1's in parents - that is the answer
    return count # XXXX

assert num_connected_groups(5, []) == 5
assert num_connected_groups(5, [[0, 1], [0, 2], [2, 3], [3, 2], [2, 3]]) == 2
assert num_connected_groups(7, [[0, 1], [1, 2], [1, 3], [4, 5]]) == 3

def num_infected(num_computers, edges, malware_seeds):
    reference = {}
    for edge in edges:
        a, b = edge[0], edge[1]

        if a in reference and b not in reference[a]:
            reference[a].append(b)
        else:
            reference[a] = [b]

        if b in reference and a not in reference[b]:
            reference[b].append(a)
        else:
            reference[b] = [a]

    counter = 0
    seeds = malware_seeds[:]
    seen = set()
    while seeds:
        current = seeds.pop()
        if current in seen:
            continue
        else:
            seen.add(current)
            counter += 1

        if current in reference:
            for x in reference[current]:
                seeds.append(x)

    return counter

assert num_infected(5, [], [0, 1]) == 2
assert num_infected(5, [[0, 1], [0, 2], [2, 3]], [0]) == 4
assert num_infected(7, [[0, 1], [1, 2], [1, 3], [4, 5]], [1, 5]) == 6
