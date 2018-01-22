
"""
  Clean up folder
"""
import os,shutil

if __name__ == '__main__':
  for file_name in os.listdir(os.path.join('dir_path','folder_name')):
    path = os.path.join('dir_path','folder_name',file_name)
    try:
      if o.path.isfile(path):
        os.unlink(path)
      elif os.path.isdir(path):
        shutil.rmtree(path)
    except Exception as e:
      print(e)
       
