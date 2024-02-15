def max_crossing_subarr(prices, low, mid, high):
    left_sum = float('-inf')
    max_left = mid
    total = 0

    for i in range(mid, low - 1, -1):
        total += prices[i]
        if total > left_sum:
            left_sum = total
            max_left = i

    right_sum = float('-inf')
    max_right = mid + 1
    total = 0

    for j in range(mid + 1, high + 1):
        total += prices[j]
        if total > right_sum:
            right_sum = total
            max_right = j

    return max_left, max_right, left_sum + right_sum


def max_subarr(prices, low, high):
    if low == high:
        return low, high, prices[low]

    mid = (low + high) // 2

    left_low, left_high, left_sum = max_subarr(prices, low, mid)
    right_low, right_high, right_sum = max_subarr(prices, mid + 1, high)
    cross_low, cross_high, cross_sum = max_crossing_subarr(prices, low, mid, high)

    if left_sum >= right_sum and left_sum >= cross_sum:
        return left_low, left_high, left_sum
    elif right_sum >= left_sum and right_sum >= cross_sum:
        return right_low, right_high, right_sum
    else:
        return cross_low, cross_high, cross_sum


def trade_price(day, prices):
    price_changes = [prices[i + 1] - prices[i] for i in range(len(prices) - 1)]    # Calculate price changes between consecutive days

    low, high, _ = max_subarr(price_changes, 0, len(price_changes) - 1) # DnC to find max sum subarray

    return day[low], day[high + 1] #Return days with best trading price


# Example usage
day = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16]
price = [100, 113, 110, 85, 105, 102, 86, 63, 81, 101, 94, 106, 101, 79, 94, 90, 97]
spacing = 3
indent_day = (" " * spacing).join(map(str,day))

best_trading_days = trade_price(day, price)
print("Days:     ", indent_day)
print("Price:", price)
print("Best trading days:", best_trading_days)
