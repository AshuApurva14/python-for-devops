
import paramiko

# Create SSH client
client = paramiko.SSHClient()

# Set policy to automatically add hosts to known hosts FileExistsError
client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
