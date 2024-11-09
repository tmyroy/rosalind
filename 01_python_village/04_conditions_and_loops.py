# Given: Two positive integers a and b (a<b<10000 ).
# Return: The sum of all odd integers from a through b , inclusively.

def sum_of_odds_one_liner(a, b):
    return sum(i for i in range(a, b + 1) if i % 2 == 1)

def sum_of_odds(a, b):
    total = 0
    for num in range(a, b + 1):
        if num % 2 == 1:
            total += num
    return total



a, b = 100, 200
print("Sum of odds (classic for loop):", sum_of_odds(a, b))
print("Sum of odds (one liner): ", sum_of_odds_one_liner(a, b))