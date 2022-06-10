import os

files = os.listdir()

for file in files:
    if file.startswith('temps'):
        print(file.split('_').[1])
