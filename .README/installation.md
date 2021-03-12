# Instalacion de Arch

## 1.- Descargar Arch

descargar arch desde la [pagina oficial](https://archlinux.org/)

## 2.- Booteable

- crear pendrive booteable con [balenaEtcher](https://www.balena.io/etcher/)
- anadir ISO a pendrive booteable con [VENTOY](https://www.ventoy.net/en/index.html)

## 3.- Instalacion

### recomendacion

Recomendado seguir los pasos de la [arch wiki](https://wiki.archlinux.org/index.php/installation_guide) con los siguientes pasos adicionales para uefi.

### particiones

al momento de formatear los discos usar gdisk.

|comando|funcion|
|---|---|
|```o```|regenerar tabla de particiones (borrar particiones)|
|```n```|nueva particion|
|```w```|escribir cambios|
|```?```|todos los comandos|

se deben crear particiones:

|particion|code|
|---|---|
|```EFI```|```ef00```|
|```SWAP```|```8200```|
|```/```|```8300```|
|```/home```|```8300```|

### Sistemas de ficheros

Hacer sistemas de ficheros:
|particion|comando|
|---|---|
|```EFI```|```mkfs.fat -F32 /dev/sdxY```|
|```SWAP```|```mkswap /dev/sdxY```|
|```/```|```mkfs.ext4 /dev/sdxY```|
|```/home```|```mkfs.ext4 /dev/sdxY```|

### montaje

ubicacion para montar.

|particion|Punto de Montaje|
|---|---|
|```/```|```/mnt```|
|```EFI```|```/mnt/efi```|
|```/home```|```/mnt/home```|

### Activar swap

```shell
swapon /dev/sdxY
```

### Descargar en el nuevo sistema

obligatorio:

```shell
pacman -S nano sudo grub efibootmgr os-prober networkmanager intel-ucode/amd-ucode base-devel
```

en caso de tener un [raid](https://wiki.archlinux.org/index.php/installation_guide#Initramfs)

```shell
pacman -S mdadm
mkinitcpio -P
```

ejecutar:

```shell
systemctl enable NetworkManager
```

### Instalacion de grub

si el firmware de la mother no es muy complejo instalar tal como dice la [wiki](https://wiki.archlinux.org/index.php/GRUB)

en caso de que el firmware de la motherboard no reconozca probar con las siguientes maneras:

```shell
grub-install --target=x86_64-efi --efi-directory=/efi --removable --recheck
```

esto creara el directorio /efi/EFI/... con el nombre de BOOT, permitiendo que la placa lo reconozca.

Opcion alternativa aun no probada:

```shell
grub-install --target=x86_64-efi --efi-directory=/efi --bootloader-id=Microsoft --recheck
```

finalmente generar la configuracion con

```shell
grub-mkconfig -o /boot/grub/grub.cfg
```

### Configuraciones adicionales antes de reiniciar

anadir usuario

```shell
useradd -m {user_name}
```

cambiarle contrasena al nuevo usuario

```shell
passwd {user_name}
```

darle permisos al nuevo usuario

```shell
usermod -aG wheel,video,audio,storage {user_name}
```

descomentar sudo:

```shell
nano /etc/sudoers
```

recomendado copiar git y realizar descargas de [configuration.md](configuration.md)

---
|[Menu Principal](../README.md)|
|:-:|
