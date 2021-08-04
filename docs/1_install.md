---
sort: 1
permalink: /installation
---

# Installation


## With installer

The installer will download the scripts and place them in `~/bin`.

```bash
curl https://telatin.github.io/biofu/installer.sh | bash
```


## From source

```bash
git clone https://github.com/telatin/biofu
cd biofu
chmod +x bin/*
```

Then place the scripts in a directory in your path, for example

```
sudo cp bin/* /usr/local/bin/
```
