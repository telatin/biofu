---
sort: 2
permalink: /usage
---

# Tools

## rev

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

## sample

`sample.py` is a script to extract the sample name from a filename.

The input filename are split using a set of characters and recomposed specifying a set
of fields.

## trimcommon

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