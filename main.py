#automation testing

#import
import requests #http requests
from bs4 import BeautifulSoup #for executing web scraping
import smtplib #building e-mail body
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import datetime #system date and time manipulation
from env_vars import __PsswdEmail__,__UserEmail__

#extract the system datetime
now = datetime.datetime.now()

#email content holder
content = ''

#Extrack Hacker News Stories
#Extract the front-page info
def extract_news(url):
    print('Extracting Hackers News Stories....')
    cnt_var = ''
    cnt_var += ('<b>HN Top Stories:</b>\n'+'<br>'+'-'*50+'<br>')
    response = requests.get(url)
    content_local = response.content
    soup = BeautifulSoup(content_local, 'html.parser')

    for i, tag in enumerate(soup.find_all('td', attrs={'class': 'title', 'valign': ''})):
        cnt_var += ((str(i + 1) + ' :: ' + tag.text + "\n" + '<br>') if tag.text != 'More' else '')
        #print(tag.prettify) #find_all('span', attrs={'class':'sitestr'}))

    return cnt_var

#Extracting the content from extract_news() function
cnt = extract_news('https://news.ycombinator.com/')
content += cnt
content += '<br>-------------------</br>'
content += '<br><br>End of Message'

#composing the E-Mail
#parameters for email authentication
#Enviormentals Windows Variables for Hiding Passwords
SERVER = 'smtp.gmail.com' #smpt server
PORT = 587 #Gmai port number
FROM = __UserEmail__
TO = 'cortezgonzalez74@gmail.com'
PASS = __PsswdEmail__

#fp = open(file_name, 'rb')
#Create a text/plain message
#msg = MIMEText('')
msg = MIMEMultipart()

#msg.add_header('Content-Disposition', 'attachment', filename='empty.txt')
msg['Subject'] = 'Top News Stories Hackers News [Automated-Email]' + ' ' + str(now.day) + ' ' + str(now.month) + ' ' + str(now.year)
msg['From'] = FROM
msg['To'] = TO
msg.attach(MIMEText(content, 'html'))
#fp.close()
print('Initialing Server......')

#authentication section
server = smtplib.SMTP(SERVER, PORT)
server.set_debuglevel(1)
server.ehlo()
server.starttls()
server.login(FROM, PASS)
server.sendmail(FROM, TO, msg.as_string())
print('Email Sent.......')
server.quit()

##CONTINUAR
##https://www.youtube.com/watch?v=s8XjEuplx_U
##Minuto: 35:04 min






