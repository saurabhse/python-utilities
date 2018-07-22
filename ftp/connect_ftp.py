import paramiko

def connect():
  key = paramiko.RSAKey.from_private_key_file(host_key)
  user = ""
  password=""
  proxy_comm = "ssh -o UserKnownHostsFile= -o StrictHostKeyChecking=no -i /dsa_key -l user_name sftpproxy nc <ftp_loc_host_name> <port>"
  proxy = paramiko.ProxyCommand(proxy_command)
  transport = paramiko.Transport(proxy)
  transport.connect()
  transport.set_hexdump(True)
  transport.auth_publickey(username=user,key=key)
  transport.auth_password(username=user, password=password)
  return paramiko.SFTPClient.from_transport(transport)
  
 if __name__ == "main":
    connect()
  
