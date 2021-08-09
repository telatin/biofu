---
sort: 2
permalink: /list
---
 
## Utilities

Every Python utility comes with a `--help` option.

### rev

`rev.py` is a script to generate the filename of the reverse pair of a given file.

Example:
```
rev.py file_R1.fastq.gz
```

Will produce:
```
file_R2.fastq.gz
```

Throwing an error if the input file was not found (unless using `--force`), or
if the autodetected reverse file was not fonund, or if the file did not contain
the specified tags.

### sample

`sample.py` is a script to extract the sample name from a filename.

The input filename are split using a set of characters and recomposed specifying a set
of fields. Given a filename like `sample_S1_R1.fastq.gz`, the script will
return `sample`, but it can be configured as where to split and which fields to join.

### trimcommon

`trimcommon.py` is a script to trim the common prefix and suffix of a list of strings/files.

Example:
```
Sample_1.fastq.gz Sample_2.fastq.gz Sample_3.fastq.gz
```

Will return:
```
1
2
3
```

## Conda Tools

### conda-list-bins

Given a Conda package, returns (or saves) a list of all the binaries it installs.
By default it will search in the conda-forge and bioconda channels, but this can be
overridden with `-c CHANNEL`. To save to file, use either `-o FILE` or `-s` (will save
the list to _packagename.txt_ in the current directory).

```
USAGE: conda-list-bins [options] package-name
```