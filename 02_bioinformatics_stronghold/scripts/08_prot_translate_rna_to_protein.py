#!/usr/bin/env python

# Given: An RNA string s corresponding to a strand of mRNA (of length at most 10 kbp).
# Return: The protein string encoded by s.


from Bio.Seq import Seq


def rna_to_protein(rna_sequence):
    rna_seq = Seq(rna_sequence)
    protein_seq = rna_seq.translate(to_stop=True)
    return str(protein_seq)


rna_sequence = "AUGGCCAUGGCGCCCAGAACUGAGAUCAAUAGUACCCGUAUUAACGGGUGA"
print(rna_to_protein(rna_sequence))
