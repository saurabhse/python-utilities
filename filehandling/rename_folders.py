import os,sys
dir = 'root_dir'
for path, dirs, files in os.walk(dir, topdown=True):
    if 'text_to_replace' in path:
        print(path)
        new_path = path.replace('text_to_replace','new_text')
        os.rename(path,new_path)

for path, dirs, files in os.walk(dir, topdown=True):
    if 'text_to_replace' in path:
        print(path)
