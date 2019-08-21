import datetime
from apscheduler.schedulers.blocking import BlockingScheduler
from apscheduler.schedulers.background import BackgroundScheduler
import time


def job2(text):
    print('job2', datetime.datetime.now(), text)

scheduler = BackgroundScheduler()
job = scheduler.add_job(job2, 'date', run_date=datetime.datetime(2019, 8, 21, 16, 40, 0), args=['text'], id='job2')
job = scheduler.add_job(job2, 'date', run_date=datetime.datetime(2019, 8, 21, 16, 41, 0), args=['text'], id='job1')
job = scheduler.add_job(job2, 'date', run_date=datetime.datetime(2019, 8, 21, 16, 42, 0), args=['text'], id='job3')
job = scheduler.add_job(job2, 'date', run_date=datetime.datetime(2019, 8, 21, 16, 43, 0), args=['text'], id='job4')
scheduler.start()

#print scheduler.get_jobs()
#job.remove()
print scheduler.get_jobs()
time.sleep(3660)
print "1min"
