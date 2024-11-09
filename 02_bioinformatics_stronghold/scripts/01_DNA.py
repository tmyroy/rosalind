#!/usr/bin/env python

# Given: A DNA string s of length at most 1000 nt.
# Return: Four integers (separated by spaces) counting the respective number of times that the symbols 'A', 'C', 'G', and 'T' occur in s.

from collections import Counter

def count_bases(s):
    c = Counter(s)
    return ' '.join(str(c[base]) for base in ['A', 'C', 'G', 'T'])


input_path = '02_bioinformatics_stronghold/data/input/01_dna.txt'
output_path = '02_bioinformatics_stronghold/data/output/01_dna.txt'

with open(input_path, 'r') as infile, open(output_path, 'w') as outfile:
    dna_string = infile.read().strip()
    outfile.write(count_bases(dna_string))