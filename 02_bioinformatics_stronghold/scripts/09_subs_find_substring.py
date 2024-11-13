#!/usr/bin/env python

# Given: Two DNA strings s and t (each of length at most 1 kbp).
# Return: All locations of t as a substring of s.

import re

def find_substring_locations(s, t):
    return " ".join(str(m.start() + 1) for m in re.finditer(f"(?={t})", s))

s = "GATATATGCATATACTT"
t = "ATAT"
print(find_substring_locations(s, t))
