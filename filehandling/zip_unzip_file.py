import zipfile,os

def zip():
  zf = zipfile.ZipFile(os.path.join("path","output_file"), mode='w')
  try:
     zf.write(os.path.join("path","input_file"),arcname="input_file")
  except:
     print("error")
  finally:
      zf.close()
      
def unzip():
  zip_ref = zipfile.ZipFile(os.path.join("myzippedfile.zip"), 'r')
  zip_ref.extractall(os.path.join("folder_path")
  zip_ref.close()

if __name__ == 'main':
  unzip()
