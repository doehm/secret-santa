# SECRET SANTA

# LIBRARIES
import os
import numpy as np,
import datetime
import pandas as pd
import smtplib

# DATE AND TIME
dt = datetime.datetime.now()
date = dt.strftime('%Y-%m-%d at %I:%M%p')
datem = dt.strftime('%Y-%m-%d')

# EMAIL DICTIONARY
# replace the names and emails with those participating
fam = {
'Alice'   : 'alice@gmail.com',
'Bob'     : 'bob@gmail.com',
'Chris'   : 'chris@gmail.com',
'Daniel'  : 'daniel@hotmail.com',
'Evelyn'  : 'evelyn@gmail.com',
'Fred'    : 'fred@gmail.com'
}

# SELECT SECRET SANTAS
santa = list(np.random.choice(list(fam.keys()), len(list(fam.keys())), replace = False))
recvr = []
for k in range(-1, len(santa)-1):
	recvr.append(santa[k])
			
# TESTING FOR ACCURATE SELECTIONS
for k in range(len(fam)):
	print santa[k] != recvr[k]
			
# STARTING EMAILS
smtpObj = smtplib.SMTP('smtp.gmail.com', 587)
smtpObj.ehlo()
smtpObj.starttls()
eml = raw_input('Enter your email: ')
pwd = raw_input('Enter login details: ')
smtpObj.login(eml, pwd)

# SENDING EMAILS
for k in range(len(fam)):
	smtpObj.sendmail(eml, fam[santa[k]], \
	'Subject: Secret Santa 2018 \
	\nHo Ho Ho %s! \
	\n\nChristmas is almost here, \
	\nTime to find that Christmas cheer! \
	\n\nThis year you are buying for....... %s! \
	\n\nThis was sent on %s. \
	\n\nDan' % (santa[k], recvr[k], date))

# QUIT SERVER
smtpObj.quit()

# STORE SELECTIONS FOR SAFE KEEPING
santadf = pd.DataFrame({'santa':santa, 'recvr':recvr})
santadf.to_csv('Secret Santa list ' + datem + '.csv')
