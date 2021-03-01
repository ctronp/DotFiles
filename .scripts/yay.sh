#!/bin/bash

sudo pacman -S --needed git base-devel

tmpf="/tmp"
if [ ! -d "$tmpf/autoinstalacion" ]; then
    mkdir $tmpf/autoinstalacion
fi

tmpf=$tmpf/autoinstalacion


cd $tmpf

git clone https://aur.archlinux.org/yay.git

cd yay

makepkg -si
