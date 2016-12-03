#APO Automailer 
#For Lukas and Nikki
#
#V 1.00
#Updated: 11/12/2016 6:42 PM
#Written by Luke Xing
#
#
#V 1.00 -- 11/12/2016 6:42 PM -- Created

from email.mime.text import MIMEText
from datetime import date
import smtplib
import csv
import passwords as pw

#Opening CSV
def sort_standing():
    trainPath = "C:/Users/Luke Xing/Dropbox/Programming/Python/APO/apo_hours.csv"
    trainData = []
    with open(trainPath) as trainCsv:
        trainReader = csv.reader(trainCsv, delimiter=',', quotechar='"')
        for row in trainReader:
            trainData.append(row)
			
    return(trainData)

#Defining a method to create a list to sort
hours_log = sort_standing()
if hours_log[0][2] =='Hours':
	del hours_log[0]

#Getting a list of people
def hours_gb(hours_log):
	low_hours_names = []
	low_hours_email = []
	low_hours_hours	= []
	
	
	for member in hours_log:
		if float(member[2]) < 7:
			low_hours_names.append(member[0])
			low_hours_email.append(member[1])
			low_hours_hours.append(member[2])
	
	dunce_list = []
	dunce_list.extend((low_hours_names,low_hours_email,low_hours_hours))
	
	return dunce_list
	
	

SMTP_SERVER = "smtp.gmail.com"
SMTP_PORT = 587

#Username & Password
SMTP_USERNAME = pw.email
SMTP_PASSWORD = pw.password

#Change to membershipAPO
EMAIL_FROM = "darcartisan@gmail.com"

EMAIL_SUBJECT = "Low Hours Alert"

DATE_FORMAT = "%m/%d/%Y"
#EMAIL_SPACE = ", "
	
#Email Body
EMAIL_TO_LIST = hours_gb(hours_log)

'''
def send_email():
    msg = MIMEText(DATA)
    msg['Subject'] = EMAIL_SUBJECT + " %s" % (date.today().strftime(DATE_FORMAT))
    msg['To'] = EMAIL_SPACE.join(EMAIL_TO)
    msg['From'] = EMAIL_FROM
    mail = smtplib.SMTP(SMTP_SERVER, SMTP_PORT)
    mail.starttls()
    mail.login(SMTP_USERNAME, SMTP_PASSWORD)
    mail.sendmail(EMAIL_FROM, EMAIL_TO, msg.as_string())
    mail.quit()
'''
	
def mailsender():
	
	max = len(EMAIL_TO_LIST[0])
	for i in range(0,max):

		name = EMAIL_TO_LIST[0][i]
		hours_req = '7'
		hours = EMAIL_TO_LIST[2][i]
		vpmem1 = 'Nikki Kijak'
		vpmem2 = 'Lukas Hager'
		
		msg = ("Dear %s, you have %s hours.  You need to have %s by this point."
			"Please see %s or %s for details.") %(name, hours, hours_req, vpmem1, vpmem2)
			
		msg['Subject'] = EMAIL_SUBJECT + " %s" % (date.today().strftime(DATE_FORMAT))
		mail = smtplib.SMTP(SMTP_SERVER, SMTP_PORT)
		msg['To'] = EMAIL_TO_LIST[1][i]
		msg['From'] = EMAIL_FROM
		mail = smtplib.SMTP(SMTP_SERVER, SMTP_PORT)
		mail.starttls()
		mail.login(SMTP_USERNAME, SMTP_PASSWORD)
		mail.sendmail(EMAIL_FROM, EMAIL_TO, msg.as_string())
		mail.quit()

#Sending some emails
if __name__=='__main__':
	#print(EMAIL_TO_LIST)
    mailsender()