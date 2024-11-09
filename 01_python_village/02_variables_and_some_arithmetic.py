#!/usr/bin/env python3

# Given: Two positive integers a and b, each less than 0
# Return: Integer corresponding to the square of the hypotenuse of the right triangle whose legs have lengths a and b.


def hypotenuse_square(a, b):
    return a**2 + b**2


a = 3
b = 5
print(hypotenuse_square(a, b))

