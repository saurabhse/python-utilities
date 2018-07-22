import connect_ftp
import os,shutil

def check_for_file(sftp,file_name_to_check,max_attempts,wait_time):
  attempts = max_attempts
  while(max_attempts > 0):
      if file_name_to_check in sftp.listdir():
        return True
      else:
        attempts = attempts -1 
        time.sleep(wait_time)

def update_file_name(ftp,file_name_to_update,new_file_name):
    try:
      ftp.rename(file_name_to_update,new_file_name)
    except:
      print("error")


def get_file(sftp,file_name,file_format):
  file = sftp.open(file_name + file_format,'r')
  shutil.copyfileobj(file, open(os.path.join("destination_folder_path",file_name,file_format),'wb'))
  
def direct_fetch_file():
    sftp.get(file_name + file_format,os.path.join("destination_folder_path",file_name,file_format))

if __name__ == "main":
  check_for_file(connect_ftp.connect(),"abc.txt",2,2)
  get_file(connect_ftp.connect(),"abc","txt")
