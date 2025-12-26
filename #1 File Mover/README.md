# Move Files to a Specific Directory

Move files with a specific format 

## Run in Terminal

## Run in Current Directory

Run this command in terminal to move files in your current directory

```bash
python fileHandling.py
```

## Run Program Globally

You can run this in terminal and organize your file by follow these steps:

1. **Add executable permission**
```bash
chmod +x fileHandling.py
```

2. **Link the file**
```bash
ln -s /path/to/your/code/fileHandling.py ~/.local/bin/organize
```

3. **Refresh Terminal**

Refresh your terminal

4. **Run Command**
```bash
organize
```
or
```bash
organize [format] [folder]
```

NOTE: Run this command for help
```bash
organize --help
#or
organize --h
```

Now you can run this program wherever its directory is.