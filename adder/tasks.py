from celery import Celery
import os

app = Celery('tasks', broker=os.environ['REDISGREEN_URL'], backend=os.environ['REDISGREEN_URL'])

import time
@app.task
def add(x, y):
    return x + y

@app.task
def doin_work(val):
    time.sleep(3)
    return val + 3
