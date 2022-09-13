# 367 Skill Tracker // StatTrak

## Arch System Pref for Dev

## Apps
 - Docker
 - VS Code
 - DBeaver

```sh
// Install the following packages
$ sudo pacman -Syu
$ sudo pacman -S git docker docker-compose go code base-devel 

$ reboot
```

```
// Start docker and enable it on boot
$ sudo systemctl start docker.service
$ sudo systemctl enable docker.service

// Add docker to account so sudo isnt needed
$ sudo usermod -aG docker $USER

$ reboot
```

Happy
```sh
$ cd Downloads
$ git clone https://aur.archlinux.org/snapd.git
$ cd snapd
$ makepkg -s
$ sudo pacman -U snapd-2.57.2-1-x86_64.pkg.tar.zst 
$ sudo systemctl enable snapd
$ reboot
$ sudo snap install spotify

$ cd Downloads
$ git clone https://aur.archlinux.org/gti.git
$ cd gti
$ makepkg -s
$ sudo pacman -U gti-1.7.0-2-x86_64.pkg.tar.zst
$ gti pull
```

Req. for Live Share
```sh
$ sudo pacman -S gcr liburcu openssl-1.0 krb5 zlib icu gnome-keyring libsecret desktop-file-utils xorg-xprop

$ cd Downloads
$ git clone https://aur.archlinux.org/icu69.git
$ makepkg -s
$ sudo pacman -U icu69-69.1-1-x86_64.pkg.tar.zst 

```


VSCode extensions
 - ESLint
 - Git Lens
 - Go
 - Material Icon Theme
 - Tokyo Night
 - Rest Client
 - YAML
 - Docker
 - DotENV
 - TabOut
 - Live Share