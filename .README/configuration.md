# Configuracion de Arch y Qtile

configuracion e instalacion de paquetes, para la configuracion de arch y qtile. En caso de no usar qtile se pueden quitar varios paquetes aqui descargados.

## 1.- descargar paquetes

descargamos los siguientes paquetes de forma obligatoria (incluire los de la instalacion, evitar en caso de haberlos instalados previamente)
algunas fonts pueden ser retiradas.

```shell
sudo pacman -S zsh alacritty udiskie ntfs-3g vlc python-pip ttf-dejavu ttf-liberation ttf-droid ttf-croscore gnu-free-fonts ttf-croscore noto-fonts noto-fonts-emoji noto-fonts-cjk noto-fonts-extra xorg-fonts-misc xorg-server lightdm lightdm-gtk-greeter lightdm-webkit2-greeter xorg-xinit xorg-xrandr git firefox xdg-utils arandr zip unzip exa fish nodejs npm neovim ranger flameshot xsel fzf ripgrep fd the_silver_searcher ruby rubygems prettier scrot imagemagick rofi pulseaudio pavucontrol notification-daemon
```

los paquetes pueden ser revisados en mas detalle [aqui](paquetes.md)

- pudimos descargar vscode con ```code``` pero recomiendo bajarlo por [snap](https://snapcraft.io/install/code/arch) para anadir el codigo propietario.

- tambien es posible anadir xorg-apps en caso de que algunas aplicaciones lo necesiten.

descargamos los siguientes paquetes de forma recomendada

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
yay -S nerd-fonts-ubuntu-mono ccat universal-ctags-git
```

### descargas pip

recomendado para neovim/ranger (no recuerdo cual de los dos)

```shell
pip install neovim ueberzug pylint
```

### descargas npm

recomendado para neovim (js).

```shell
sudo npm i -g neovim
```

### descargas gem

recomendado para neovim

```shell
gem install neovim
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

para cambiar bash por zsh o fish

```shell
chsh -s /bin/zsh
chsh -s /bin/fish
```

es posible ver todas las shells con ```chsh -l```

Pendiente por redactar...

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
pacman -S volumeicon
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

## NEOVIM y RANGER

neovim y ranger ya fueron descargados e instalados previamente
comenzamos realizando un enlace simbolico de neovim a vim

```shell
cd \bin

sudo ln nvim vim
```

copiar configuracion de ranger y ejecutar script tras cambiarle permisos.

```shell
chmod 755 ~/.config/ranger/install-plugs.sh
~/.config/ranger/install-plugs.sh
```

### comandos de vim

remplazar (se usa [regex](https://vim.fandom.com/wiki/Search_and_replace))
configuraciones de vim en [/user/.config/nvim/](https://github.com/ctronp/DotFiles/tree/main/user/.config/nvim)

```vim
solo en la linea
:s/original/final/g

en todo el texto
:%s/original/final/g
```

split (abre otro archivo)

```vim
horizontal
:split ~/path/to/file.c

vertical
:split ~/path/to/file.c
```

para moverse entre ventana

```vim
ctrl + [hjkl]
```

para cerrar ventana

```vim
:bd
```

cambiar tamano

```vim
alt + [hjkl]
```

cambiar de buffer/ventana sobrepuesta

```vim
Tab
```

mover linea

```vim
shift + [jk]
```

modificar en NERDTree

```vim
m
```

instalar complementos coc (dentro de vim)

```vim
:CocInstall coc-clangd coc-eslint coc-cmake coc-fzf-preview coc-git coc-go coc-java coc-json coc-julia coc-markdownlint coc-python coc-sh coc-sql
```

### Fork original (aun no lo modifico, pego el original)

archivo original de [antonio sarosi](https://github.com/antoniosarosi/dotfiles/blob/master/.config/nvim/README.md)

To use this config, first download some dependencies:
el siguiente comando debe ser ejecutado al comienzo, antes de iniciar vim.

```bash
# Vim-plug
sh -c 'curl -fLo "${XDG_DATA_HOME:-$HOME/.local/share}"/nvim/site/autoload/plug.vim --create-dirs \
       https://raw.githubusercontent.com/junegunn/vim-plug/master/plug.vim'

# Some runtimes are needed, install only those you don't have
sudo pacman -S nodejs npm python python-pip ruby rubygems

# Download neovim packages
pip install neovim
gem install neovim
sudo npm i -g neovim

# Some other dependencies
sudo pacman -S xsel fzf ripgrep fd the_silver_searcher prettier
yay -S universal-ctags-git
```

Now open *neovim* and execute *:PlugInstall*. Close *neovim*, and next time
you open it all my configs should be applied. This are some keybingins besides
default ones:

| Key                    | Action                                 |
| ---------------------- | -------------------------------------- |
| **jk** or **kj**       | Go to normal mode (from insert)        |
| **alt + [hjkl]**       | Resize split                           |
| **control + [hjkl]**   | Navigate splits                        |
| **control + s**        | Save                                   |
| **control + q**        | Save and quit                          |
| **tab**                | Next buffer                            |
| **shift + tab**        | Previous buffer                        |
| **control + b**        | Close buffer                           |
| **shift + <** or **>** | Indent one level or remove it (visual) |
| **shift + k** or **j** | Move selected line down or up (visual) |

***Plugin keybindings***:

| Key           | Action                                        |
| ------------- | --------------------------------------------- |
| **space + f** | Fuzzy search                                  |
| **space + /** | Comment selected line or block                |
| **space + n** | Toggle NerdTree                               |
| **space + p** | Format document with prettier                 |
| **shift + k** | Function or class documentation and arg types |
