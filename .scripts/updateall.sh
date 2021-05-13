#!/bin/bash

needSudo="sudo"

if [ "$EUID" -eq 0 ]; then
    needSudo=""
fi


# Not sudo updates

which conda && conda update --all && conda update conda

which yay && yay -Sy && yay -Syu

# sudo updates

which pacman && eval "$needSudo pacman -Syy" && eval "$needSudo pacman -Syyu"

which snap && eval "$needSudo snap refresh"
