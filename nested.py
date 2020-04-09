#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Module docstring: One line description of what your program does.
"""
__author__ = "Christian Rojas"

import sys


def is_nested(line):
    """Validate a single input line for correct nesting"""
    open_paren = ['(', '[', '{', '<', '(*']
    close_paren = [')', ']', '}', '>', '*)']

    paren_stack = []
    counter = 0

    while line:
        token = line[0]
        if line.startswith("(*"):
            token = "(*"
        elif line.startswith("*)"):
            token = "*)"
        
        counter += 1
        line = line[len(token):]

        if token in open_paren:
            paren_stack.append(token)
        elif token in close_paren:
            close_item = close_paren.index(token)
            open_item = open_paren[close_item]
            if paren_stack.pop() != open_item:
                return "NO: " + str(counter)

    if paren_stack:
        return "NO: " + str(counter)
    else:
        return "YES"


def main(args):
    """Open the input file and call `is_nested()` for each line"""
    # Results: print to console and also write to output file
    with open('input.txt', 'r') as f:
        with open('output.txt', 'w') as o:
            for line in f:
                output_txt = is_nested(line)
                print is_nested(line)
                o.write(output_txt + '\n')


if __name__ == '__main__':
    main(sys.argv[1:])
