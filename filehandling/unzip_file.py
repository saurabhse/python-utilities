import zipfile,os

def unzip():
  zip_ref = zipfile.ZipFile(os.path.join("myzippedfile.zip"), 'r')
  zip_ref.extractall(os.path.join("folder_path")
  zip_ref.close()

if __name__ == 'main':
  unzip()
