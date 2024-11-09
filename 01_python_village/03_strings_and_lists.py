#!/usr/bin/env python3

# Given: A string s of length at most 200 letters and four integers a, b, c and d.
# Return: The slice of this string from indices a through b and c through d (with space in between), inclusively. In other words, we should include elements s[b] and s[d] in our slice.

def slice_string(s, a, b, c, d):
    first_slice = s[a:b+1] 
    second_slice = s[c:d+1]
    return f"{first_slice} {second_slice}"

s = "wmypl9BTAjkxeyrAZChrysemys17GWsTRHh96XNt95PbjMPQbelliirToPRwFDmCptfD3spCJyBKErT1KeZsWvD7WUFFLfymttVoRRq5Xm22NgMxnuf9MbmGlZ0xQ3j1k9wtpx8bR6m6sirEjKvk1tHU0cJualRLGz1sKEq1Y29bhheRdsFtqMVRmwEhqqUKMLAlz."
a, b, c, d = 17, 25, 48, 53
print(slice_string(s, a, b, c, d))

