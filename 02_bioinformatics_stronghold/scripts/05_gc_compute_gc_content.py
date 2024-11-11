#!/usr/bin/env python

# Given: At most 10 DNA strings in FASTA format (of length at most 1 kbp each).
# Return: The ID of the string having the highest GC-content, followed by the GC-content of that string. Rosalind allows for a default error of 0.001 in all decimal answers unless otherwise stated; please see the note on absolute error below.

from Bio import SeqIO
from Bio.SeqUtils import gc_fraction

def find_highest_gc_content(fasta_file):
    max_gc_label = None
    max_gc_content = 0.0
    
    for record in SeqIO.parse(fasta_file, "fasta"):
        gc_content_value = gc_fraction(record.seq) * 100
        if gc_content_value > max_gc_content:
            max_gc_content = gc_content_value
            max_gc_label = record.id
    
    return max_gc_label, max_gc_content



input_path = "02_bioinformatics_stronghold/data/input/05_gc.txt"
output_path = "02_bioinformatics_stronghold/data/output/05_gc.txt"

with open(input_path, "r") as infile, open(output_path, "w") as outfile:
    label, gc_content_value = find_highest_gc_content(infile)
    outfile.write(f"{label}\n{gc_content_value}")
