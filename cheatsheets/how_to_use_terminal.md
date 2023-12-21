---
marp: true
class: invert
---

# Basic usage of the terminal on macOS (and Linux) 

The following is a cheatsheet for how to use the most basic commands on a macOS-system. These commands are mostly the same on Linux/UNIX/macOS. 

For explanation on how to use Windows-commands see further down...

---


### Navigation:

- `pwd`: Print working directory (displays the current directory path).
- `ls`: List files and directories in the current directory.
  - `ls -l`: Detailed list view.
  - `ls -a`: List all files, including hidden ones.

- `cd`: Change directory.
  - `cd <directory>`: Move to a specific directory.
  - `cd ..`: Move up one directory.
  - `cd ~`: Move to the home directory.

---

### File and Directory Operations:

- `mkdir <directory_name>`: Create a new directory.
- `touch <file_name>`: Create a new empty file.
- `cp <source> <destination>`: Copy files or directories.
  - `cp -r <source_directory> <destination_directory>`: Recursive copy.

- `mv <source> <destination>`: Move or rename files or directories.
- `rm <file>`: Remove a file.
  - `rm -r <directory>`: Remove a directory and its contents (use with caution).


---


### Viewing and Editing Files:

- `cat <file>`: Display the contents of a file.
- `more <file>`: Display the contents of a file one screen at a time.
- `less <file>`: View and navigate through the contents of a file.
- `nano <file>` or `vim <file>`: Open a text editor to create or edit a file.

---

### System Information:

- `top`: Display real-time system information and running processes.
- `df -h`: Show disk space usage.
- `free -h`: Display free and used memory in a human-readable format.

---

### Running Programs:

- `./<program>`: Run an executable file in the current directory.
- `open <file>`: Open a file with its default application.
- `open .`: Opens the finder in the current directory.
- `chmod +x <file>`: Make a file executable.

---

### Searching:

- `find <directory> -name <filename>`: Search for a file in a directory.
- `grep <pattern> <file>`: Search for a pattern in a file.
  - `grep -r <pattern> <directory>`: Recursive search in a directory.

---

### Network:

- `ping <host>`: Send a network request to a host.
- `ifconfig` or `ipconfig`: Display network configuration information.

### SSH:

- `ssh <username>@<hostname>`: Connect to a remote server via SSH.

---

### Process Management:

- `ps`: Display information about running processes.
- `kill <process_id>`: Terminate a process.

This is a basic overview, and there are many more commands and options available. You can explore more by checking the manual pages using the `man` command (e.g., `man ls` for information about the `ls` command).

---

## Difference between macOS/Linux/Windows

While many commands are similar across different operating systems, there are variations between macOS (which is Unix-based), Linux, and Windows. Here's how some of the commands from the initial list might differ:


---

### Navigation:

- **Print Working Directory:**
  - macOS/Linux: `pwd`
  - Windows: `cd`

- **List Files:**
  - macOS/Linux: `ls`
  - Windows: `dir`

- **Change Directory:**
  - macOS/Linux: `cd <directory>`
  - Windows: `cd <directory>` or just `<directory>`

---

### File and Directory Operations:

- **Make Directory:**
  - macOS/Linux: `mkdir <directory_name>`
  - Windows: `mkdir <directory_name>`

- **Copy:**
  - macOS/Linux: `cp <source> <destination>`
  - Windows: `copy <source> <destination>`

- **Move:**
  - macOS/Linux: `mv <source> <destination>`
  - Windows: `move <source> <destination>`

---

- **Remove:**
  - macOS/Linux: `rm <file>`
  - Windows: `del <file>` or `erase <file>`

---

### Viewing and Editing Files:

- **Display Contents:**
  - macOS/Linux: `cat <file>`
  - Windows: `type <file>`

- **Open Text Editor:**
  - macOS/Linux: `nano <file>` or `vim <file>`
  - Windows: `notepad <file>` or `start notepad <file>`

---

### System Information:

- **Top:**
  - macOS/Linux: `top`
  - Windows: `tasklist` or `wmic process get name`

- **Disk Space:**
  - macOS/Linux: `df -h`
  - Windows: `wmic logicaldisk get size,freespace,caption`

- **Memory:**
  - macOS/Linux: `free -h`
  - Windows: `systeminfo`

---

### Running Programs:

- **Run Executable:**
  - macOS/Linux: `./<program>`
  - Windows: `<program>.exe`

- **Open File:**
  - macOS/Linux: `open <file>`
  - Windows: `start <file>`

---

### Searching:

- **Find:**
  - macOS/Linux: `find <directory> -name <filename>`
  - Windows: `dir /s /b <directory>\<filename>`

- **Grep:**
  - macOS/Linux: `grep <pattern> <file>`
  - Windows: `findstr /C:<pattern> <file>`

---

### Network:

- **Ping:**
  - macOS/Linux: `ping <host>`
  - Windows: `ping <host>`

- **Network Configuration:**
  - macOS/Linux: `ifconfig`
  - Windows: `ipconfig`

---

### SSH:

- **SSH:**
  - macOS/Linux: `ssh <username>@<hostname>`
  - Windows: Use SSH from PowerShell or install third-party tools like PuTTY.

---

### Process Management:

- **List Processes:**
  - macOS/Linux: `ps`
  - Windows: `tasklist`

- **Kill Process:**
  - macOS/Linux: `kill <process_id>`
  - Windows: `taskkill /PID <process_id>`

---