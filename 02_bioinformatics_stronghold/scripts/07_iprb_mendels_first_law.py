#!/usr/bin/env python

# Given: Three positive integers k, m, and n, representing a population containing k+m+n organisms: k individuals are homozygous dominant for a factor, m are heterozygous, and n are homozygous recessive
# Return: probability that two randomly selected mating organisms will produce an individual possessing a dominant allele (and thus displaying the dominant phenotype). Assume that any two organisms can mate.


def calculate_probability_of_dominant_allele(k, m, n):
    total_pop = k + m + n

    prob_k_k = (k / total_pop) * ((k - 1) / (total_pop - 1)) * 1.0
    prob_k_m = (k / total_pop) * (m / (total_pop - 1)) * 1.0
    prob_k_n = (k / total_pop) * (n / (total_pop - 1)) * 1.0
    prob_m_k = (m / total_pop) * (k / (total_pop - 1)) * 1.0
    prob_m_m = (m / total_pop) * ((m - 1) / (total_pop - 1)) * 0.75
    prob_m_n = (m / total_pop) * (n / (total_pop - 1)) * 0.5
    prob_n_k = (n / total_pop) * (k / (total_pop - 1)) * 1.0
    prob_n_m = (n / total_pop) * (m / (total_pop - 1)) * 0.5

    dominant_probability = (
        prob_k_k + prob_k_m + prob_k_n + 
        prob_m_k + prob_m_m + prob_m_n + 
        prob_n_k + prob_n_m
    )

    return dominant_probability


k, m, n = 27, 15, 19
print(calculate_probability_of_dominant_allele(k, m, n))