#!/usr/bin/env python3
import shutil
import os
import re
import argparse

filePath = os.getcwd()

files = [x for x in os.listdir(filePath) if os.path.isfile(os.path.join(filePath, x))]

def main():
    parser = argparse.ArgumentParser(prog='organize', description='Move files to a directory')

    parser.add_argument('extension', nargs='?', help='File\'s format to move (e.g., pdf, etc.)')
    parser.add_argument('folder', nargs='?', help='Destination directory name')

    args = parser.parse_args()

    if args.extension and args.folder:
        format = args.extension
        targetPath = args.folder
    else:
        format = str(input('Enter file\'s format: '))
        targetPath = str(input('Target directory: '))

    r = re.compile(f'.*.{format}')
    fileName = list(filter(r.match, files))

    if len(fileName) == 0:
        print('There is no matched file\'s format')
        exit()
    
    try:
        os.makedirs(targetPath, exist_ok=True)
        if not os.path.isdir(targetPath):
            print(f'Directory {targetPath} created successfully.')
    except PermissionError:
        print(f'Permission denied: Unable to create {targetPath}')
        exit()
    except Exception as e:
        print(f'An error occurred: {e}')
        exit()

    try:
        for x in fileName:
            shutil.move(x, f'{filePath}/{targetPath}/{x}')
        print('Your files is now organized.')
    except Exception as e:
        print(f'An error occurred: {e}')
    
if __name__ == '__main__':
    main()