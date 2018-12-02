def bottom_up(rods_values):
    r = [0]
    cut_pos = [0]
    for i in range(1, len(rods_values)):
        # print(i)
        max_value = -2 ** 31
        pos = 0
        for j in range(1, i + 1):
            last_max=max_value
            max_value = max(max_value, r[i - j] + rods_values[j][1])
            if last_max!=max_value:
                pos = j
        r.append(max_value)
        cut_pos.append(pos)
    return r,cut_pos


if __name__ == '__main__':
    rod_values = [(0, 0), (1, 1), (2, 5), (3, 8), (4, 9), (5, 10), (6, 17), (7, 17), (8, 20), (9, 24), (10, 30)]
    print(bottom_up(rod_values))
    pass
