# Descarga y configuracion de tema e iconos GTK

[como obtener archivos GTK](https://wiki.archlinux.org/index.php/GTK#Configuration)
[transferir estilos de GTK a Qt](https://wiki.archlinux.org/index.php/Uniform_look_for_Qt_and_GTK_applications)

## tema

primero descargamos un conjunto de [temas](https://www.gnome-look.org/p/1316887/)

de estos elegire Material-Black-Pistachio_1.9.2.zip

este archivo zip lo descomprimiremos, y la carpeta resultante la moveremos y le cambiaremos el nombre a algo mas simple.

```shell
cd ~/Downloads
unzip Material-Black-Pistachio-3.36_1.9.2.zip
mv ~/Downloads/Material-Black-Pistachio-3.36 ~/.themes/Material-Pistacho
```

luego introducimos el nombre del tema en los siguientes archivos:

- [.gtkrc-2.0](/../.gtkrc-2.0)
- [.config/gtk-3.0/settings.ini](/../.config/gtk-3.0/settings.ini)

## iconos

primero descargamos un conjunto de [iconos](https://www.gnome-look.org/p/1333360/)

de estos elegire Material-Black-Pistachio-Suru_1.9.2.zip

este archivo zip lo descomprimiremos, y la carpeta resultante la moveremos y le cambiaremos el nombre a algo mas simple.

```shell
cd ~/Downloads
unzip Material-Black-Pistachio-Suru_1.9.2.zip
mv ~/Downloads/Material-Black-Pistachio-Suru ~/.icons/Material-Pistacho-Suru
```

luego introducimos el nombre del tema en los siguientes archivos:

- [.gtkrc-2.0](/../.gtkrc-2.0)
- [.config/gtk-3.0/settings.ini](/../.config/gtk-3.0/settings.ini)
