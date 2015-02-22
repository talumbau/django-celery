from celery import Celery

app = Celery('tasks', broker='redis://localhost', backend='redis://localhost:6379/0')

import time
@app.task
def add(x, y):
    return x + y

@app.task
def doin_work(val):
    time.sleep(3)
    return val + 9
