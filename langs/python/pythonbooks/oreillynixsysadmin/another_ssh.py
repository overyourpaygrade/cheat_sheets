#!/usr/bin/env python

import paramiko
import os

def conn(hostname,port,username,password):
    # Connect and run a command
    s = paramiko.SSHClient()
    s.load_system_host_keys()
    s.connect(hostname,port,username=username,password=password)
    stdin,stdout,stderr = s.exec_command('sudo ifconfig')
    print stdout.read()
    s.close()

def conn_priv(hostname,port,username,pkey_file):
    # Connect and run a command
    key = paramiko.RSAKey.from_private_key_file(pkey_file)
    s = paramiko.SSHClient()
    s.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    s.load_system_host_keys()
    s.connect(hostname,port,username=username,pkey=key)
    stdin,stdout,stderr = s.exec_command('sudo ifconfig')
    print stdout.read()
    s.close()

def copy(hostname,port,username,password,dir_path):
    t = paramiko.Transport((hostname,port))
    t.connect(username=username,password=password)
    sftp = paramiko.SFTPClient.from_transport(t)
    files = sftp.listdir(dir_path)
    for f in files:
        print 'Retrieving', f
        sftp.get(os.path.join(dir_path, f), f)
    t.close()

def copy_priv(hostname,port,username,pkey_file,dir_path):
    key = paramiko.RSAKey.from_private_key_file(pkey_file)
    t = paramiko.Transport((hostname,port))
    t.connect(username=username,pkey=key)
    sftp = paramiko.SFTPClient.from_transport(t)
    files = sftp.listdir(dir_path)
    for f in files:
        print 'Retrieving', f
        sftp.get(os.path.join(dir_path, f), f)
    t.close()

def main():
    hostname = '192.168.1.25'
    port = 22
    username = 'pi'
    password = 'rasberry'
    dir_path = '/home/pi/get'
    pkey_file = '/home/SoulEater/.ssh/raspimon'

    #conn(hostname,port,username,password)

    conn_priv(hostname,port,username,pkey_file)

    #copy(hostname,port,username,password,dir_path)

    copy_priv(hostname,port,username,pkey_file,dir_path)

if __name__ == "__main__":
    main()
