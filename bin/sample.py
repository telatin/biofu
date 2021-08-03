#!/usr/bin/env python3
"""
Extract the sampleID from filename(s)
"""
import sys, os
import argparse
from pprint import pprint

def eprint(*args, **kwargs):
    """
    Print to stderr
    """
    print(*args, file=sys.stderr, **kwargs)

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__,
        formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument('FILE', nargs='+',
        help='Input file(s)')
    parser.add_argument('-s', '--split-char', help='Split chars', nargs='*', default=['_', '.'])
    parser.add_argument('-f', '--fields', nargs='*', help='Fields to extract (comma separated)', default=[0])
    parser.add_argument('-j', '--join-char', help='Join fields with this char [default: _]', default='_')
    parser.add_argument('--force', help='Ignore non existing input files', action='store_true')
    parser.add_argument('--verbose', help='Verbose mode', action='store_true')
    opts = parser.parse_args()

    samples = []

    for f in opts.FILE:
        if not os.path.isfile(f) and not opts.force:
            print('Error: {} is not a file'.format(f))
            sys.exit(f"ERROR: Input file not found: {f}")

        basename = os.path.basename(f)
        # split f at all the chars in the split_chars list, store in a list
        # and remove empty strings
        parts = [basename]
        for c in opts.split_char:
            temp = []
            for index, element in enumerate(parts):
                # append all elements of split
                temp.extend(element.split(c))
            parts = temp
        
        # join elements of args.fields as new string
        sample = ""
        for i in opts.fields:
            sample +=  parts[int(i)]
            if i != opts.fields[-1]:
                sample += opts.join_char
        
        if opts.verbose:
            eprint(f"{sample}\t{basename}")
        samples.append(sample)
    
    # Check for duplicates in samples
    if len(set(samples)) != len(samples) and not opts.force:
        
        sys.exit(f"ERROR: Duplicate sample names found: {', '.join(samples)}")
    else:
        print(*samples, sep='\n')