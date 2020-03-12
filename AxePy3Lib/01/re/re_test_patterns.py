#!/usr/bin/env python3
# encoding: utf-8
#
# Copyright (c) 2010 Doug Hellmann.  All rights reserved.
#
"""Show all matches for a list of patterns.
"""

# end_pymotw_header
import re


def test_patterns(text, patterns):
    """Given source text and a list of patterns, look for
    matches for each pattern within the text and print
    them to stdout.
    """
    # Look for each pattern in the text and print the results
    for pattern, desc in patterns:
        print("'{}' ({})\n".format(pattern, desc))
        print("  '{}'".format(text))
        for match in re.finditer(pattern, text):
            s = match.start()
            e = match.end()
            substr = text[s:e]
            # n_backslashes = text[:s].count('\\')
            # prefix = '.' * (s + n_backslashes)
            prefix = '.'*s
            print("  {}'{}'".format(prefix, substr))
        print()
    return


if __name__ == '__main__':
    test_patterns('abbaaabbbbaaaaa', [('ab', "'a' followed by 'b'"),
                                      ('ba', "'b' followed by 'a'")])
    print("-----------------------")
    text = 'abbaaabbbbaaaaa'
    # patts = [['a', 'b'], ['c', 'd'], ['e', 'f']]
    # patts = [('a', 'b'), ('c', 'd'), ('e', 'f')]
    # for pat, desc in patts:
    patts = {'ab': '12', 'ba': '21', 'aba': '121'}
    for pat, desc in patts.items():
        print("pat is {0!r}, desc is {1!r}".format(pat, desc))
        for match in re.finditer(pat, text):
            s = match.start()
            e = match.end()
            substr = text[s:e]
            print(s, e, substr)