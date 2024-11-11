#!/usr/bin/env python

# Given: At most 10 DNA strings in FASTA format (of length at most 1 kbp each).
# Return: The ID of the string having the highest GC-content, followed by the GC-content of that string. Rosalind allows for a default error of 0.001 in all decimal answers unless otherwise stated; please see the note on absolute error below.


input_path = "02_bioinformatics_stronghold/data/input/05_gc.txt"
output_path = "02_bioinformatics_stronghold/data/output/05_gc.txt"


def parse_fasta(fasta_data):
    sequences = {}
    label = None
    for line in fasta_data.strip().splitlines():
        if line.startswith(">"):
            label = line[1:].strip()
            sequences[label] = ""
        else:
            sequences[label] += line.strip()
    return sequences


def gc_content(sequence):
    gc_count = sequence.count("G") + sequence.count("C")
    return (gc_count / len(sequence)) * 100


def highest_gc_content(fasta_data):
    sequences = parse_fasta(fasta_data)
    max_gc_label = None
    max_gc_content = 0.0

    for label, sequence in sequences.items():
        gc = gc_content(sequence)
        if gc > max_gc_content:
            max_gc_content = gc
            max_gc_label = label

    return max_gc_label, max_gc_content


with open(input_path, "r") as infile, open(output_path, "w") as outfile:
    fasta_data = infile.read().strip()
    label, gc_content_value = highest_gc_content(fasta_data)
    outfile.write(f"{label}\n{gc_content_value}")
