#!/usr/bin/env python3
"""
Generate the reverse paired end filename, return error
if not found.   
"""

import os, sys
import argparse

def eprint(*args, **kwargs):
    """
    Print to stderr
    """
    print(*args, file=sys.stderr, **kwargs)

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('-f', '--forward-tag', dest='fwd', 
        help='forward read tags', nargs='+', default=["_R1" ,"_1."])
    parser.add_argument('-r', '--reverse-tag',  nargs='+', dest='rev', 
        help='reverse read tags, comma separated', default=["_R2" ,"_2."])
    parser.add_argument('-a', '--absolute', help="return absolute path", action='store_true')
    parser.add_argument('-v', '--verbose', action='store_true',help='print verbose output')
    parser.add_argument('FILE', help='file to check')
    args = parser.parse_args()

    # Check that the input file exists, if not, exit
    if not os.path.isfile(args.FILE):
        sys.exit("ERROR: R1 not found: '{}'".format(args.FILE))
    else:
        if args.verbose:
            eprint("INFO: Input file found {}".format(args.FILE))
    
    # Generate reverse filenames, exit if not found
    for forTag, index in zip(args.fwd, range(len(args.fwd))):
        if forTag in args.FILE:
            if args.verbose:
                eprint("INFO: Forward tag {} found {}".format(forTag, args.FILE))
            revFile = args.FILE.replace(forTag, args.rev[index])
            if revFile == args.FILE:
                sys.exit("ERROR: Reverse file is equal to input: '{}'".format(args.FILE))
            if not os.path.isfile(revFile):
                sys.exit("ERROR: R2 not found: '{}'".format(revFile))
            else:
                if args.verbose:
                    eprint("INFO: Reverse file found {}".format(revFile))
                if args.absolute:
                    revFile = os.path.abspath(revFile)
                else:
                    # Normalise the path
                    revFile = os.path.normpath(revFile)
                print(revFile)
                exit(0)
    