#!/usr/bin/env python5
# -*- coding: utf-8 -*-

# Filename: module_1_practice.py

# Practice exercise for exercises 1-10
# from the book Learn Python the Hard Way (third edition)

# This is an exercise for Module 1
# Please fix each error in this program!

work_days = "Mon Tue Wed Thu Fri"
weekend_days = "Sat Sun"
all_days = work_days + " " + weekend_days

print("All days are: %s" % all_days)

num_days = 7

print("A week has %d days and these are: %s" % (num_days, all_days))





# Errors
# ln 2: utf-X -> utf-8
# ln 10: not commented
# ln 12: missing double quote after 'Fri'
# ln 13: missing '='
# ln 14: missing '+' after '" "'
# ln 16: missing closed bracket after 'all_days'
# ln 20: missing '%' after string and variables for formatting
# ln 20: missing closed bracket after '(num_days, all_days)'
# ln 18/20: either initiate 'num_days' with 7, and not '7', so it is an int
#           or change '%d' to '%s' in line 20, so the '7' can be printed out