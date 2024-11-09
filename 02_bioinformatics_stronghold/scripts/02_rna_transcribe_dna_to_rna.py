#!/usr/bin/env python

# Given: A DNA string t having length at most 1000 nt.
# Return: The transcribed RNA string of t.

def transcribe_dna_to_rna(s):
    return dna_string.replace('T', 'U')


input_path = '02_bioinformatics_stronghold/data/input/02_rna.txt'
output_path = '02_bioinformatics_stronghold/data/output/02_rna.txt'

with open(input_path, 'r') as infile, open(output_path, 'w') as outfile:
    dna_string = infile.read().strip()
    outfile.write(transcribe_dna_to_rna(dna_string))