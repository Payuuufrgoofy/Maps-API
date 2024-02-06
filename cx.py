import schedule
import datetime

def job():
    dt = datetime.datetime.now()
    hour = datetime.datetime.timetuple(dt)[3]
    i = hour % 12 if hour % 12 else 12
    print('Ку' * i)

schedule.every().minute.at(':00').do(job)

while True:
    schedule.run_pending()
