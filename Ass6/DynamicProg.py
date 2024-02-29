#6481323

def findMax(prices, n):
    revenue = [0] * (n + 1)

    for i in range(1, n + 1):
        max_revenue = -1
        for j in range(1, i + 1):
            max_revenue = max(max_revenue, prices[j - 1] + revenue[i - j])
        revenue[i] = max_revenue
    return revenue[n]

prices = [1, 3, 3, 6, 7, 9, 9, 10, 11, 12, 14, 15]
n = len(prices)

max_revenue = findMax(prices, n)
print("Prices:",prices)
print("Rod length: ",n)
print("Maximum revenue:",max_revenue)
