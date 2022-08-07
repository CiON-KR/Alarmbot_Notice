import requests 
import telegram
import urllib3
import datetime
import time
from bs4 import BeautifulSoup
from apscheduler.schedulers.blocking import BlockingScheduler

def job_function():  
    bot = telegram.Bot(token='***********************************')
	chat_id = -*************
	url = requests.get('https://sejong.korea.ac.kr/campuslife/notice/college', verify=False)
	data = BeautifulSoup(url.content, 'html.parser')
	table = data.find('p',{'class':'title'})
	trs = table.find_all('a')
	content = trs[0].text.strip()
	with open ('Update_Notice.txt', 'r+') as f_read :
		before = f_read.readline()
		if before != content :
			for t in trs :
				adrs = t.attrs['href']
				sejong = "sejong.korea.ac.kr" + adrs
			now = datetime.date.today().strftime('%Y-%m-%d')
			run = bot.sendMessage(chat_id = chat_id, text = content + '\n' + "[DATE] " + now + '\n' + "[URL] " + sejong)
            f_read.close()
            
    with open ('Update_Notice.txt', 'w+') as f_write :
        f_write.write(content)
        f_write.close()
    
sched = BlockingScheduler()
sched = BlockingScheduler(timezone='Asia/Seoul')
sched.add_job(job_function,'cron', hour='9-18', minute='*/15')
sched.start()