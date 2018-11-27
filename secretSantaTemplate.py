#SECRET SANTA

#LIBRARIES
import os
import numpy as np,
import datetime
import pandas as pd
import smtplib

#DATE AND TIME
dt = datetime.datetime.now()
date = dt.strftime('%Y-%m-%d at %I:%M%p')
datem = dt.strftime('%Y-%m-%d')

#EMAIL DICTIONARY
fam = {
'Alice'   : 'alice@gmail.com',
'Bob'     : 'bob@gmail.com',
'Chris'   : 'chris@gmail.com',
'Daniel'  : 'daniel@hotmail.com',
'Evelyn'  : 'evelyn@gmail.com',
'Fred'    : 'fred@gmail.com'
}

#SELECT SECRET SANTAS
badSelection = 1
while badSelection == 1:
	santa = list(np.random.choice(fam.keys(), len(fam), replace = False))
	recvr = list(np.random.choice(fam.keys(), len(fam), replace = False))
	badSelection = 0
	for k in range(len(fam)):
		if santa[k] == recvr[k]:
			badSelection = 1
			
#TESTING FOR ACCURATE SELECTIONS
for k in range(len(fam)):
	print santa[k] != recvr[k]
			
#STORE SELECTIONS FOR SAFE KEEPING
santadf = pd.DataFrame(fam.items(), columns = ['santa', 'recvr'])
santadf.to_csv('Secret Santa list ' + datem + '.csv')
	
#STARTING EMAILS
smtpObj = smtplib.SMTP('smtp.gmail.com', 587)
smtpObj.ehlo()
smtpObj.starttls()
eml = raw_input('Enter your email: ')
pwd = raw_input('Enter login details: ')
smtpObj.login(eml, pwd)

#SENDING EMAILS
for k in range(len(fam)):
	smtpObj.sendmail(eml, fam[santa[k]], \
	'Subject: Secret Santa 2018 \
	\nHo Ho Ho %s! \
	\n\nChristmas is almost here, \
	\nTime to find that Christmas cheer! \
	\n\nhttps://media1.giphy.com/media/yXUu66ZPiiKIM/giphy.gif?cid=3640f6095be0256954394f3432f75df3\
	\n\nThis year you are buying for....... %s! \
	\n\nThis was sent on %s. \
	\n\nDan' % (santa[k], recvr[k], date))

#QUIT SERVER
smtpObj.quit()