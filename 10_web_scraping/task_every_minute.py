"""
The basic difference between this script and the previous one is that this one runs every hour. rest of the code is the same .
Challenge => now , how to perform some task periodically ?
Thought => There is a module called <schedule>schedule that can be used to perform tasks periodically.

"""

import schedule
import time


def job():
    print("Performing task every minute")


schedule.every(1).minutes.do(job)
while True:
    print("Checking for pending tasks")
    schedule.run_pending()
    time.sleep(1)
