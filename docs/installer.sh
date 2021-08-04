#!/bin/bash

# Check to have git installed
git --version || { echo >&2 "git is not installed. Aborting."; exit 1; }

# Check not to have biofu already here
if [ -d "biofu" ]; then
    echo "'biofu' was already downloaded here. Aborting."
    exit 1
fi
DESTINATION_DIR=${1:-$HOME/bin/}
echo "Installing BioFu to $DESTINATION_DIR"

mkdir -p $DESTINATION_DIR

# split $PATH into an array
IFS=:
read -a PATHARRAY <<< "$PATH"
IFS=$'\n'
INPATH=0

for i in "${PATHARRAY[@]}"
do
  if [[ $i == $DESTINATION_DIR ]]; then
    INPATH=1
  fi
done

if [ $INPATH -eq 0 ]; then
  if [ -e "$HOME/.bash_profile" ]; then
    echo "# source $HOME/.bash_profile"

    # if file does not contain string "BIOFU"
    if ! grep  "BIOFU" "$HOME/.bash_profile"; then
        echo "# BIOFU installer" >> $HOME/.bash_profile
        echo "export PATH=\"$DESTINATION_DIR:$PATH\"" >> $HOME/.bash_profile
    fi
  elif [ -e "$HOME/.bashrc" ]; then
    echo "# source $HOME/.bashrc"
    # if file does not contain string "BIOFU"
    if ! grep  "BIOFU" "$HOME/.bashrc"; then
        echo "# BIOFU installer" >> $HOME/.bashrc
        echo "export PATH=\"$DESTINATION_DIR:$PATH\"" >> $HOME/.bashrc
    fi
  fi
fi


set -euox pipefail
git clone https://github.com/telatin/biofu
cd biofu
chmod +x bin/*
cp -v bin/* $DESTINATION_DIR/
rm -rf biofu
