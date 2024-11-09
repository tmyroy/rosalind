#!/usr/bin/env python3

# Given: A string s of length at most 200 letters and four integers a, b, c and d.
# Return: The slice of this string from indices a through b and c through d (with space in between), inclusively. In other words, we should include elements s[b] and s[d] in our slice.


def slice_string(s, a, b, c, d):
    first_slice = s[a : b + 1]
    second_slice = s[c : d + 1]
    return f"{first_slice} {second_slice}"


s = "HumptyDumptysatonawallHumptyDumptyhadagreatfallAlltheKingshorsesandalltheKingsmenCouldntputHumptyDumptyinhisplaceagain. "
a, b, c, d = 22, 27, 97, 102
print(slice_string(s, a, b, c, d))
