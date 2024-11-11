#!/usr/bin/env python

# Given: Two DNA strings s and t of equal length (not exceeding 1 kbp).
# Return: The Hamming distance dH(s,t).

from Bio.Seq import Seq

def hamming_distance_biopython(s, t):
    s_seq = Seq(s)
    t_seq = Seq(t)
    
    return sum(a != b for a, b in zip(s_seq, t_seq))


s = "GAGCCTACTAACGGGAT"
t = "CATCGTAATGACGGCCT"
print(hamming_distance_biopython(s, t))