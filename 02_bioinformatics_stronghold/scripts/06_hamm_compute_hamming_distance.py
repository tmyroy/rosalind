#!/usr/bin/env python

# Given: Two DNA strings s and t of equal length (not exceeding 1 kbp).
# Return: The Hamming distance dH(s,t).

from Bio.Seq import Seq
from operator import ne

def hamming_distance_biopython(s, t):
    s_seq = Seq(s)
    t_seq = Seq(t)
    
    return sum(map(ne, s_seq, t_seq))


s = "GAGCCTACTAACGGGAT"
t = "CATCGTAATGACGGCCT"
print(hamming_distance_biopython(s, t))