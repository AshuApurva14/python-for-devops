
import paramiko
import os

def create_ssh_client():
try:

  hostname = os.environ.get('SSH_HOSTNAME')
  username = os.environ.get('SSH_USERNAME')
  keyfile = os.environ.get('SSH_PRIVATE_KEY')
  # Create SSH client
  client = paramiko.SSHClient()

  # Set policy to automatically add hosts to known hosts FileExistsError
  client.set_missing_host_key_policy(paramiko.AutoAddPolicy())

  # Connect to remote host
  client.connect(hostname=hostname, username=username, key_filename=keyfile)
  return client

except paramiko.AuthenticationException:
       print("Authentication Failed! Please check your hostname, username and Keyfile")


except Exception as e:
       print(f"Error Occured! {e}")
    return none


ssh_client = create_ssh_client()
if ssh_client:
    pass

