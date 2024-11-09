#!/usr/bin/env python

# Given: A DNA string s of length at most 1000 bp.
# Return: The reverse complement sc of s .

from Bio.Seq import Seq


input_path = "02_bioinformatics_stronghold/data/input/03_revc.txt"
output_path = "02_bioinformatics_stronghold/data/output/03_revc.txt"


def reverse_complement(dna_string):
    dna_seq = Seq(dna_string)
    return str(dna_seq.reverse_complement())


with open(input_path, "r") as infile, open(output_path, "w") as outfile:
    dna_string = infile.read().strip()
    outfile.write(reverse_complement(dna_string))
