def find_coins_greedy(total_sum, coins):
    result = {}
    for coin in sorted(coins, reverse=True):
        count = total_sum // coin
        if count != 0:
            result[coin] = count
        total_sum %= coin
    return result if total_sum == 0 else 'Cannot form exact sum with given coins'


def find_min_coins(total_sum, coins):
    dp = [float('inf')] * (total_sum + 1)
    dp[0] = 0  # No coins needed for sum 0
    for i in range(1, total_sum + 1):
        for coin in coins:
            if i - coin >= 0:
                dp[i] = min(dp[i], dp[i - coin] + 1)

    result = {}
    if dp[total_sum] == float('inf'):
        return 'Cannot form exact sum with given coins'

    # Trace back to find the coins used
    while total_sum > 0:
        for coin in coins:
            if total_sum >= coin and dp[total_sum] == dp[total_sum - coin] + 1:
                if coin in result:
                    result[coin] += 1
                else:
                    result[coin] = 1
                total_sum -= coin
                break
    return result


# Usage examples:
coins = [50, 25, 10, 5, 2, 1]
print("Greedy approach:", find_coins_greedy(113, coins))
print("Dynamic programming approach:", find_min_coins(113, coins))