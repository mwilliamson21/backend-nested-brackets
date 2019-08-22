#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Module docstring: One line description of what your program does.
"""
__author__ = "MWilliamson21 with help from instructor"

import sys
openers = ['[', '(', '{', '(*', '<']
closers = [']', ')', '}', '*)', '>']


def is_nested(s):
    stack = []
    for n in s:
        if n in openers:
            stack.append(n)
        if n in closers:  # for example, `}`
            matching_opener = openers[closers.index(n)]
            if len(stack) == 0 or stack.pop() != matching_opener:
                return "NO "
    if stack:  # tests if stack is empty or not
        return "NO "
    return "Yes "


def main():
    with open('input.txt') as infile:
        for line in infile:
            result = is_nested(line)
            print(result)
            # print(line)
    pass  # Guaranteed now that k gets closed automatically
    # k.close()


if __name__ == '__main__':
    main()


def valid_parentheses(string):
    stack = []
    for n in string:
        if n == "(":
            stack.append(n)
        if n == ")":
            if len(stack) == 0 or stack.pop() != "(":
                return False
    if len(stack) != 0:
        return False
    return True

