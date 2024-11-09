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


s = "When I find myself in times of trouble Mother Mary comes to me Speaking words of wisdom let it be And in my hour of darkness she is standing right in front of me Speaking words of wisdom let it be Let it be let it be let it be let it be Whisper words of wisdom let it be And when the broken hearted people living in the world agree There will be an answer let it be For though they may be parted there is still a chance that they will see There will be an answer let it be Let it be let it be let it be let it be There will be an answer let it be Let it be let it be let it be let it be Whisper words of wisdom let it be Let it be let it be let it be let it be Whisper words of wisdom let it be And when the night is cloudy there is still a light that shines on me Shine until tomorrow let it be I wake up to the sound of music Mother Mary comes to me Speaking words of wisdom let it be Let it be let it be let it be yeah let it be There will be an answer let it be Let it be let it be let it be yeah let it be Whisper words of wisdom let it be"

print(f"Word Count with Counter\n{'-' * 25}\n{word_count_with_counter(s)}")
print(f"\n\nWord Count\n{'-' * 10}\n{word_count(s)}")
