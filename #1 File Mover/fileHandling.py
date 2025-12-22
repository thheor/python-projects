import shutil
import os
import re

filePath = '/home/theo/code/learn-python/'

files = [x for x in os.listdir(filePath) if os.path.isfile(os.path.join(filePath, x))]
print(files)

r = re.compile('.*.pdf')
fileName = list(filter(r.match, files))

for x in fileName:
    shutil.move(x, f'{filePath}pdfFile/{x}')

r = re.compile('.*.txt')
fileName = list(filter(r.match, files))

for x in fileName:
    shutil.move(x, f'{filePath}txtFile/{x}')