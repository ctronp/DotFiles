#!/bin/bash

tmpf="/tmp"
if [ ! -d "$tmpf/autoinstalacion" ]; then
    mkdir $tmpf/autoinstalacion
fi

tmpf=$tmpf/autoinstalacion

cd $tmpf

curl -L https://repo.anaconda.com/miniconda/Miniconda3-latest-Linux-x86_64.sh -o miniconda3.sh

chmod u+x "./miniconda3.sh"

bash "./miniconda3.sh" -b -p "$HOME/miniconda3" -f

$HOME/miniconda3/bin/conda init fish