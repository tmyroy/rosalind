#!/usr/bin/env python

# Given: Positive integers n≤40 and k≤5
# Return: The total number of rabbit pairs that will be present after n months, if we begin with 1 pair and in each generation, every pair of reproduction-age rabbits produces a litter of k rabbit pairs (instead of only 1 pair).


def rabbit_pairs(n, k):
    F = [0] * (n + 1)
    F[1], F[2] = 1, 1

    for i in range(3, n + 1):
        F[i] = F[i - 1] + k * F[i - 2]

    return F[n]


n, k = 5, 3

print(rabbit_pairs(n, k))
