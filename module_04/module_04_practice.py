#!/usr/bin/python3
# -*- coding: utf-8 -*-

# Filename: module_4_practice.py

# Practice exercise for exercises 18-24
# from the book Learn Python the Hard Way (third edition)


def add_numbers(arg1, arg2):
    return arg1 + arg2

# def print_something(text):
#     print("Hello... %s" % text)

def print_something():
    print("Hello World!")

num1 = 34.643254353
num2 = 56.845345456
result = add_numbers(num1, num2)

print("Calculation: %r + %r = %r" % (num1, num2, result))
print_something()


# Errors
# ln 10: missing ',' between arguments
# ln 13/14: only one function
# ln 21: missing '=' after 'result', variable is not declared/initialized
# ln 23: '%i' instead of '%f'
# ln 23: '%s' or '%r' would be the best answer, to display all digits