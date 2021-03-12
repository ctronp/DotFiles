# Configuracion de Arch y Qtile

configuracion e instalacion de paquetes, para la configuracion de arch y qtile. En caso de no usar qtile se pueden quitar varios paquetes aqui descargados.

## 1.- descargar paquetes

descargamos los siguientes paquetes de forma obligatoria (incluire los de la instalacion, evitar en caso de haberlos instalados previamente)
algunas fonts pueden ser retiradas.

```shell
sudo pacman -S fish alacritty udiskie ntfs-3g vlc python-pip ttf-dejavu ttf-liberation ttf-droid ttf-croscore ttf-fira-code gnu-free-fonts noto-fonts noto-fonts-emoji noto-fonts-cjk noto-fonts-extra xorg-server lightdm lightdm-gtk-greeter lightdm-webkit2-greeter xorg-xinit xorg-xrandr git firefox xdg-utils arandr zip unzip exa ranger flameshot ripgrep fd prettier imagemagick rofi pulseaudio pavucontrol notification-daemon okular calibre poppler notepadqq chromium qtile kmix feh picom network-manager-applet libnotify
```

los paquetes pueden ser revisados en mas detalle [aqui](paquetes.md)

- pudimos descargar vscode con ```code``` pero recomiendo bajarlo por [snap](https://snapcraft.io/install/code/arch) para anadir el codigo propietario.

- tambien es posible anadir xorg-apps en caso de que algunas aplicaciones lo necesiten.

descargamos los siguientes paquetes de forma recomendada, solo en caso de que tengas grafica nvidia y te interese el codigo en cuda o ML.

```shell
sudo pacman -S nvidia lib32-nvidia-utils nvidia-settings cuda cudnn htop neofetch neovim flac
```

### descargar yay

instalacion de yay

```shell
cd /tmp
git clone https://aur.archlinux.org/yay.git
cd yay
makepkg -si
```

actualizar yay

```shell
yay
```

### descargas yay

descargas obligatorias

```shell
yay -S nerd-fonts-ubuntu-mono ccat qt5-styleplugins
```

## 2.- Habilitar qtile

instalamos qtile

```shell
sudo pacman -S qtile
```

habilitamos lightdm como display manager

```shell
sudo systemctl enable lightdm
```

en caso de que el sistema reclame otro ya existente

```shell
sudo rm /etc/systemd/system/display-manager.services
```

### Una vez iniciado qtile

para ejecutar programas

```shell
Mod4(Win) + 'r'
```

para cambiar bash por fish

```shell
chsh -s /bin/fish
```

es posible ver todas las shells con ```chsh -l```

## Descargar este git.

```shell
cd ~
git remote add origin https://github.com/ctronp/dotfiles.git
git pull --rebase origin main
```

en caso de error, por ejemplo al tomar el branch master (siguiente parte no comprobada)

```shell
git checkout main
git branch -d master
```

en caso de ingresar la url erroneamente.

```shell
git remote set-url origin https://github.com/ctronp/dotfiles.git
```

### configuraciones manuales de programas

audio (recomendado reinicial luego de instalar)

```shell
pacman -S --needed pulseaudio pavucontrol
```

wallpaper

```shell
pacman -S --needed feh
```

brillo

```shell
pacman -S brightnessctl
```

transparencia

```shell
pacman -S picom
```

icono de volumen

```shell
pacman -S kmix
```

arandr (configuracion de monitores, almacenar comando permanente en .xprofile)

```shell
pacman -S arandr
```

icono de internet

```shell
pacman -S network-manager-applet
```

icono de bateria

```shell
pacman -S cbatticon
```

### notificaciones

descargamos el programa

```shell
pacman -S libnotify
```

creamos el siguiente archivo e introduciomos lo siguiente

```shell
nano /usr/share/dbus-1/services/org.freedesktop.Notifications.service

[D-BUS Service]
Name=org.freedesktop.Notifications
Exec=/usr/lib/notification-daemon-1.0/notification-daemon
```

## configuraciones adicionales

### defaults apps

modificar ~/.config/mimeapps.list para aplicaciones default
se recomienda hacer un link de este a ~/.local/share/applications/mimeapps.list para aplicaciones antiguas

```shell
ln -sf ~/.config/mimeapps.list ~/.local/share/applications/mimeapps.list
```

esto solucionara problemas como al abrir links desde telegram.

## instalacion de temas e iconos

para mas detalle de esta configuracion verificar el siguiente [link](themes.md)

## configuracion de fish

fish ya fue descargado previamente, al inicio de esta pagina.
descargar [oh my fish](https://github.com/oh-my-fish/oh-my-fish)

```shell
curl -L https://get.oh-my.fish | fish
```

y luego descargar un tema

ver temas

```shell
omf themes
```

instalar un tema

```shell
omf install spacefish
```

---
|[Menu Principal](../README.md)|
|:-:|
