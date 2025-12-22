#!/usr/bin/env python3
import shutil
import os
import re

filePath = os.getcwd()

print('Current path:', filePath)

files = [x for x in os.listdir(filePath) if os.path.isfile(os.path.join(filePath, x))]

while True:
    format = str(input('Enter file\'s format: '))

    r = re.compile(f'.*.{format}')
    fileName = list(filter(r.match, files))

    if len(fileName) == 0:
        print('There is no matched file\'s format')
    else:
        break

targetPath = str(input('Target directory: '))

try:
    os.mkdir(targetPath)
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
    