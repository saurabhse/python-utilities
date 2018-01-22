"""
  Count the number of lines in the file
"""
import subprocess

if __name__ == '__main__':
  try:
      count = subprocess.call(['wc','-l','file_name'])
  except Exception as e:
      print(e)
      
