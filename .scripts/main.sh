#!/bin/bash

tmpf="/tmp"
if [ ! -d "$tmpf/autoinstalacion" ]; then
    mkdir $tmpf/autoinstalacion
fi

tmpf=$tmpf/autoinstalacion


# Actualizacion de paquetes pacman

sudo pacman -Sy
sudo pacman -Syu

# Instalacion de paquetes pacman

sudo pacman -S --needed fish alacritty udiskie ntfs-3g vlc python-pip ttf-dejavu ttf-liberation ttf-droid \ 
ttf-croscore ttf-fira-code gnu-free-fonts noto-fonts noto-fonts-emoji noto-fonts-cjk noto-fonts-extra \ 
xorg-server lightdm lightdm-gtk-greeter lightdm-webkit2-greeter xorg-xinit xorg-xrandr git firefox \ 
xdg-utils arandr zip unzip exa ranger flameshot ripgrep fd prettier imagemagick rofi pulseaudio \ 
pavucontrol notification-daemon okular calibre poppler notepadqq chromium qtile kmix feh picom \ 
network-manager-applet libnotify nano-syntax-highlighting

sudo pacman -S --needed nvidia lib32-nvidia-utils nvidia-settings cuda cudnn htop neofetch neovim flac

# Instalacion de gestores de paquetes

$HOME/.scripts/miniconda.sh
$HOME/.scripts/yay.sh

# Instalacion de paquetes yay

yay -Sy
yay -Syu

yay -S nerd-fonts-ubuntu-mono ccat qt5-styleplugins

# Configuracion de escritorio

sudo systemctl enable lightdm
chsh -s /bin/fish

ln -sf $HOME/.config/mimeapps.list $HOME/.local/share/applications/mimeapps.list
curl -L https://get.oh-my.fish | fish
omf install spacefish