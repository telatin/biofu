# BioFu

[![BioFu Repository](https://img.shields.io/github/last-commit/telatin/biofu)](https://github.com/telatin/biofu)

A simple list of command line utilities 
to be used to simplify the work of bioinformaticians.

Some design concepts to make this tiny repository easily portable:
 * Depending on Python 3.6 and its standard library, avoiding external libraries


## Example

I often write loops like this:

```bash
set -euo pipefail
for FILE in dir/*_R1.fastq.gz;
do
  REV=${FILE/_R1/_R2}
  SAMPLE=$(basename $FILE | cut -f 1 -d _)
  programme -1 $FILE -2 $REV -o $SAMPLE.txt
done
```

What if I change the input to `another_dir/*_1.fq`?
I also need to change the `REV` variable substitution, otherwise I
would pass as second pair the very same forward file.

```bash
set -euo pipefail
for FILE in dir/*_R1.fastq.gz;
do
  REV=$(rev.py $FILE)
  SAMPLE=$(sample.py $FILE)
  programme -1 $FILE -2 $REV -o $SAMPLE.txt
done
```

`rev.py` will exit with error if the reverse file is not found (unless `--force` is passed)
or if the imputed filename is equal to the forward file, and by default substitutes both `_R1`
and `_1.` so it works with most commonly used files.
