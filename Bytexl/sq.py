def spy_problem(house_money):
    n = len(house_money)

    if n == 0:
        return 0, []

    def max_money(arr):
        incl, excl = 0, 0
        positions = []

        for i in range(len(arr)):
            new_excl = max(incl, excl)
            incl = excl + arr[i]
            excl = new_excl

            if incl > excl:
                positions.append(i + 1)

        return max(incl, excl), positions

    if n == 1:
        return house_money[0], [1]

    if n == 2:
        return max(house_money), [house_money.index(max(house_money)) + 1]

    max_money_1, positions_1 = max_money(house_money[:-1])

    max_money_2, positions_2 = max_money(house_money[1:])

    if max_money_1 > max_money_2:
        return max_money_1, positions_1
    else:
        positions_2 = [pos + 1 for pos in positions_2]
        return max_money_2, positions_2


input_data = list(map(int, input().split()))
result, positions = spy_problem(input_data)
print(result)
print(positions)
