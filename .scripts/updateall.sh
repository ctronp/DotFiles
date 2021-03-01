#!/bin/bash

needSudo="sudo"

if [ "$EUID" -eq 0 ]; then
    needSudo=""
fi

which pacman && eval "$needSudo pacman -Sy" && eval "$needSudo pacman -Syu"

which conda && conda update --all && conda update conda

which snap && eval "$needSudo snap refresh"

which yay && yay -Sy && yay -Syu