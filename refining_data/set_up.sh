#!/usr/bin/env bash

# Author: hyunyoung2(github id)

# This shell script is for setting up of normalizing original file of wikimedia and divided a file into each file of doc tage(<doc id=...> ... </doc>


tar -zxvf original.tar.gz

./iteration_basic_normalization.sh

python3 divided.py 
