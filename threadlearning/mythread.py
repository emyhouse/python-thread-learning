# coding=utf-8

import threading
import time

def job(name, wait_time):
    for i in range(10):
        print("job {}:count={}".format(name, i))
        time.sleep(wait_time)


def start_threads():
    threads = []
    for i in range(20):
        job_name = "job{}".format(i)
        t = threading.Thread(target=job, args=(job_name,0))
        t.start()
        threads.append(t)
    return threads
