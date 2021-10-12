import schedule
import time
import os
import sys

os.system('node g.js http://uve.usep.edu.ph http.txt 600 GET PHPSESSID:gq15q5ho3eqq6gatdqm6nqdva5')

def job():
    os.system('node g.js http://uve.usep.edu.ph http.txt 600 GET PHPSESSID:gq15q5ho3eqq6gatdqm6nqdva5')
    
schedule.every(1).seconds.do(job)

while True:
    schedule.run_pending()
    time.sleep(1)