

def coinChange(self, coins, amount):
    """
    :type coins: List[int]
    :type amount: int
    :rtype: int
    """

    V = [-1 for _ in range(0, amount + 1)]
    V[0] = 0 # you need 0 coins for 0 amount
    coins = sorted(coins)

    for m in range(1, amount + 1):
        min_coins = -1
        for c in coins:
            if (m - c) < 0:
                break  # since all the coins from now will be too large
            elif V[m - c] != - 1:
                if min_coins == -1 or V[m - c] < min_coins:
                    min_coins = V[m - c]

        # add one for the additional coin:
        if min_coins != -1:
            V[m] = min_coins + 1
    print(V)

    return V[amount]


coins = [2]
amount = 3
self = None
print(coinChange(self, coins, amount))



