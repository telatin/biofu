#!/usr/bin/env python3
"""
Given a set of strings, remove the shared prefixes/suffixes
"""

import sys

VERSION = "0.2"

def eprint(*args, **kwargs):
    """
    Print to stderr
    """
    print(*args, file=sys.stderr, **kwargs)

def stripSharedEnds(stringList):
    """
    Remove the common characters shared by all the strings of stringList
    """

    # Remove common prefixes
    start = 0
    while charEqualInList(stringList, start):
        start += 1
    if start > 0:
        stringList = removeNchars(stringList, start)
    
    
    # Remove common suffixes
    end = -1
    while charEqualInList(stringList, end):
        end -= 1
    if end < -1:
        stringList = removeNchars(stringList, end + 1)   
     
    # Return the new list 
    return stringList

def charEqualInList(list, n):
    """
    Return true if the nth character of all the strings in list are equal
    """
    for index, string in enumerate(list):
        if len(string) >= abs(n) and len(list[0]) >= abs(n):
            if string[n] != list[0][n]:
                return False
        else:
            eprint(f"{abs(n)}¬{string}¬Index {index} has a string of length {len(string)}")
            return False
    return True


def removeNchars(list, n):
    """
    Remove the first (positive n)/last (negative n)
    characters of all the strings in list
    """
    newlist = []
    # remove first char of string

    for string in list:
        if n >= 0:
            string = string[n:]
        else:
            string = string[:n]
        newlist.append(string)
    return newlist




if __name__ == "__main__":
    import argparse
    import os
    
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('strings', nargs='+', help='strings to trim')
    parser.add_argument('-b', '--basename', action='store_true', help="Treat input strings as paths and take the basename")
    parser.add_argument('--verbose', action='store_true', help='Verbose mode')
    # Add version
    parser.add_argument('--version', action='version', version="%(prog)s " + VERSION)
    args = parser.parse_args()

    inputList = args.strings
    
    if len(inputList) < 2:
        eprint("WARNING: Not enough strings to compare (minimum 2)")
        print(inputList[0])
        sys.exit(0)

    if args.basename:
        inputList = [os.path.basename(string) for string in inputList]
    if args.verbose:
        print("Input:\n -", "\n - ".join(args.strings))
    
    outputList = stripSharedEnds(inputList)


    print("\n".join(outputList))