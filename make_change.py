# based on https://github.com/codingforinterviews/practice-problems/tree/master/coin_change

from functools import lru_cache


def parse_input(input):
    lines = input.splitlines()

    if len(lines) != 2:
        raise "invalid input"

    coins = tuple(map(int, lines[0].split(', ')))
    amount = int(lines[1].split(', ')[0])

    return coins, amount


@lru_cache
def get_number_of_change_variants_dp(coins, amount, min_coin):
    print(coins, amount, min_coin)

    if amount == 0:
        return 1
    elif amount < 0:
        return 0

    count = 0
    for coin in coins:
        if coin < min_coin:
            continue
        if amount - coin >= 0:
            count += get_number_of_change_variants_dp(
                coins, amount - coin, coin)

    return count


def get_number_of_change_variants(input):
    coins, amount = parse_input(input)

    return str(get_number_of_change_variants_dp(coins, amount, 0))


def trace(x):
    print(x)
    return x


def test():
    input = '''1, 2, 3
4'''
    output = '''4'''

    assert(trace(get_number_of_change_variants(input)) == output)


test()
