#!/usr/bin/python3
# -*- coding: utf-8 -*-

# Filename: module_2_practice.py

# Practice exercise for exercises 11-14
# from the book Learn Python the Hard Way (third edition)

from sys import argv

script, arg1, arg2 = argv

print("""
  Script    : %s
  Argument 1: %s
  Argument 2: %s
"""
% (script, arg1, arg2))

input_number = int(input("Please enter a number: "))

# Multiply 8 with the input_number variable and print the result
calc_result = 8 * input_number
print("8 * %d = %d" % (input_number, calc_result))


# Errors
# ln 9: 'from sys import arg' > 'from sys import argv
# ln 11: missing ',' (comma) after arg1
# ln 16: missing %s
# ln 20: missing bracket after '")'
# ln 23: missing '*'
# ln 24: missing '%'