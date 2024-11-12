#!/usr/bin/env python

# Given: Three positive integers k, m, and n, representing a population containing k+m+n organisms: k individuals are homozygous dominant for a factor, m are heterozygous, and n are homozygous recessive
# Return: probability that two randomly selected mating organisms will produce an individual possessing a dominant allele (and thus displaying the dominant phenotype). Assume that any two organisms can mate.


def calculate_probability_of_dominant_allele(k, m, n):
    total_pop = k + m + n
    total_pairs = total_pop * (total_pop - 1)

    dominant_probability = (
        k * (k - 1) +          # AA x AA (100% dominant offspring)
        2 * k * m +            # AA x Aa (100% dominant offspring)
        2 * k * n +            # AA x aa (100% dominant offspring)
        m * (m - 1) * 0.75 +   # Aa x Aa (75% dominant offspring)
        2 * m * n * 0.5        # Aa x aa (50% dominant offspring)
    ) / total_pairs

    return dominant_probability

k, m, n = 2, 2, 2 
print(calculate_probability_of_dominant_allele(k, m, n))