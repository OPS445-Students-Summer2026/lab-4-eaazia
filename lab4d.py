#!/usr/bin/env python3

def first_five(text):
    return str(text)[:5]

def last_seven(text):
    return str(text)[-7:]

def middle_number(number):
    text = str(number)
    return text[1:3]

def first_three_last_three(str1, str2):
    return str1[:3] + str2[-3:]
