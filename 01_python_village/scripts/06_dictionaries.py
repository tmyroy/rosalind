#!/usr/bin/env python3

# Given: A string s of length at most 10000 letters. 
# Return: The number of occurrences of each word in s, where words are separated by spaces. Words are case-sensitive, and the lines in the output can be in any order

from collections import Counter

# using Counter from collections is certainly nicer, but probably not what was intended by rosalind
def word_count_with_counter(s):
    word_counts = Counter(s.split())
    return '\n'.join(f"{word} {count}" for word, count in word_counts.items())

def word_count(s):
    word_counts = {}
    for word in s.split(' '):
        if word in word_counts:
            word_counts[word] += 1
        else:
            word_counts[word] = 1
    return '\n'.join(f"{word} {count}" for word, count in word_counts.items())


s = "We tried list and we tried dicts also we tried Zen"

print(f"Word Count with Counter\n{'-' * 25}\n{word_count_with_counter(s)}")
print(f"\n\nWord Count\n{'-' * 10}\n{word_count(s)}")
