# Configuracion de Arch y Qtile

configuracion e instalacion de paquetes, para la configuracion de arch y qtile. En caso de no usar qtile se pueden quitar varios paquetes aqui descargados.

## 1.- descargar paquetes

descargamos los siguientes paquetes de forma obligatoria (incluire los de la instalacion, evitar en caso de haberlos instalados previamente)
algunas fonts pueden ser retiradas.

```shell
sudo pacman -S fish alacritty udiskie ntfs-3g vlc python-pip ttf-dejavu ttf-liberation ttf-droid ttf-croscore gnu-free-fonts noto-fonts noto-fonts-emoji noto-fonts-cjk noto-fonts-extra xorg-server lightdm lightdm-gtk-greeter lightdm-webkit2-greeter xorg-xinit xorg-xrandr git firefox xdg-utils arandr zip unzip exa ranger flameshot ripgrep fd prettier imagemagick rofi pulseaudio pavucontrol notification-daemon
```

los paquetes pueden ser revisados en mas detalle [aqui](paquetes.md)

- pudimos descargar vscode con ```code``` pero recomiendo bajarlo por [snap](https://snapcraft.io/install/code/arch) para anadir el codigo propietario.

- tambien es posible anadir xorg-apps en caso de que algunas aplicaciones lo necesiten.

descargamos los siguientes paquetes de forma recomendada, solo en caso de que tengas grafica nvidia y te interese el codigo en cuda o ML.

```shell
sudo pacman -S nvidia lib32-nvidia-utils cuda cudnn htop neofetch neovim flac
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

habilitamos lightd como display manager

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

## Pendiente por redactar... aun pendiente por redactar

```shell
git clone este repositorio
ln git_files ~/.config
```

### configuraciones manuales de programas

audio (recomendado reinicial luego de instalar)

```shell
pacman -S pulseaudio pavucontrol
```

wallpaper

```shell
pacman -S feh
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

configurar monitores en arandr y almacenar en .xprofile

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
ln -s ~/.config/mimeapps.list ~/.local/share/applications/mimeapps.list
```

esto solucionara problemas como al abrir links desde telegram.

## instalacion de temas e iconos

se descargan los temas de gtk y se copian a ~/.theme/
se descargan los iconos de gtk y se copian a ~/.icons/

las configuraciones de [gtk](https://wiki.archlinux.org/index.php/GTK#Configuration) (para aplicar los temas) se hacen en las siguientes ubicaciones:

```shell
~/.gtkrc-2.0
~/.config/gtk-3.0/settings.ini
```

[tema e iconos](https://www.gnome-look.org/p/1316887/)

en caso de tener problemas configurando temas se puede usar lxappearance

para cursor de mouse descargar xcb-util-cursor

```shell
pacman -S xcb-util-cursor
```

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
imf install spacefish
```
