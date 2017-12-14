# coding=utf-8
from threadlearning import mythread

if __name__ == "__main__":
    threads = mythread.start_threads()
    for t in threads:
        t.join()
    print("all threads over")


