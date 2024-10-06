# Welcome to (the world of) Linux

Check out my

[Linux Cheatsheet](https://github.com/arvidjohansen/linux-cheat-sheet)

## Specialized software lists

from: https://wiki.archlinux.org/title/List_of_applications


-   [awesome-linuxaudio](https://github.com/nodiscc/awesome-linuxaudio) --- Software for audio/video/live production
-   [awesome-selfhosted](https://github.com/Kickball/awesome-selfhosted) --- Network services and web applications
-   [awesome-shell](https://github.com/alebcay/awesome-shell) --- Command-line frameworks, toolkits and guides
-   [awesome-sysadmin](https://github.com/n1trux/awesome-sysadmin) --- Software for system administrators
-   [GNOME applications](https://wiki.gnome.org/Apps)
-   [Inconsolation](https://inconsolation.wordpress.com/index/) --- Lightweight and minimalist applications reviews
-   [KDE Applications](https://kde.org/applications/)
-   [K.Mandla's blog](https://kmandla.wordpress.com/software/) --- Console applications screenshots and reviews
-   [Libre Projects](https://libreprojects.net/) --- Open source hosted web services
-   [LinApp](https://web.archive.org/web/20200530213904/http://lin-app.com/) --- Commercial applications and games for Linux
-   [PRISM Break](https://prism-break.org/en/all/) --- Software against mass surveillance
-   [Privacy Tools](https://www.privacytools.io/) --- Knowledge and tools to protect your privacy against global mass surveillance


## Working with ZIP-files
https://ioflood.com/blog/zip-linux-command/

### Basic Zip Command Usage in Linux
The zip command is a handy tool in Linux that allows you to compress files, thereby saving valuable disk space and making file transfer quicker. The basic syntax of the zip command is as follows:

```bash
zip [options] [zipfile] [file1] [file2] [...]
```

### Recursive Zipping
The -r option allows you to recursively zip directories. This means that the zip command will compress not only the specified directory but also its subdirectories and the files within those subdirectories.

Here’s an example of how to use the -r option:
```bash
zip -r archive.zip dir1/

# Output:
#  adding: dir1/ (stored 0%)
#  adding: dir1/file1.txt (deflated 14%)
#  adding: dir1/file2.txt (deflated 20%)
```
### Encryption
The -e option allows you to encrypt the zip file with a password. When you use this option, the zip command will prompt you to enter a password. The contents of the zip file will be encrypted and can only be extracted by entering the correct password.

Here’s an example of how to use the -e option:
```bash
zip -e secure.zip file1.txt

# Output:
# Enter password: 
# Verify password: 
#  adding: file1.txt (deflated 14%)
```

| Option | Description | Example |
| --- | --- | --- |
| `-r` | Recursively zip directories. | `zip -r archive.zip dir1/` |
| `-e` | Encrypt zip file with a password. | `zip -e secure.zip file1.txt` |
| `-m` | Move files into zip file. | `zip -m archive.zip file1.txt` |
| `-1` | Compress files quickly. | `zip -1 archive.zip file1.txt` |
| `-9` | Compress files slowly but with best compression. | `zip -9 archive.zip file1.txt` |
| `-f` | Freshen: only changed files. | `zip -f archive.zip` |
| `-u` | Update: only changed or new files. | `zip -u archive.zip` |
| `-d` | Delete entries from a zip file. | `zip -d archive.zip file1.txt` |
| `-j` | Junk paths: store just the name of a saved file. | `zip -j archive.zip dir1/file1.txt` |
| `-v` | Verbose mode. | `zip -v archive.zip file1.txt` |