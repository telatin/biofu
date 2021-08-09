#!/usr/bin/env python3
"""
A script to strip builds from a conda environment YAML file.
Yaml module is not used as it is not installed by default.
"""
import sys, os, argparse

def eprint(*args, **kwargs):
    """
    Print to stderr
    """
    print(*args, file=sys.stderr, **kwargs)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Strip conda.yaml from a conda recipe")
    parser.add_argument("--verbose", "-v", action="store_true", help="Be verbose")
    parser.add_argument("--dry-run", "-d", action="store_true", help="Do not write output")
    parser.add_argument("--output", "-o", help="Output file", required=True)
    parser.add_argument("--name", "-n", help="Rename environment to NAME", required=False)
    parser.add_argument("--prefix", "-p", help="Set conda prefix to PATH", required=False)
    parser.add_argument("recipe", help="The conda recipe to strip")
    args = parser.parse_args()

    recipe = args.recipe
    if not os.path.isfile(recipe):
        eprint("ERROR: {} is not a file".format(recipe))
        sys.exit(1)

    if args.prefix is not None and not os.path.isdir(args.prefix):
        eprint("ERROR: {} is not a directory".format(args.prefix))
        sys.exit(1)

    with open(recipe, "r") as f:
        lines = f.readlines()

    eprint(f"{len(lines)} lines loaded from {recipe}")

    try:
        with open(args.output, "w") as f:
            for line in lines:
                parts = line.split("=")
                
                if args.name is not None and line.startswith("name:"):
                    f.write(f"name: {args.name}\n")
                elif line.startswith("prefix:"):
                    if args.prefix is not None:
                        f.write(f"prefix: {args.prefix}\n")
                elif len(parts) == 3:
                    if parts[1] == "":
                        f.write(line)
                    else:
                        f.write("=".join(parts[:2]) + "\n")
                else:
                    f.write(line)
    except IOError as e:
        eprint("ERROR: {}".format(e))
        sys.exit(1)
    