# _*_coding:utf-8_*_
# created by Amuu on 2021/9/23

import time

def cal_time(func):
    def wrapper(*args, **kwargs):
        t1 = time.time()
        # time.sleep(2)
        result = func(*args, **kwargs)
        t2 = time.time()
        print("%s running time: %s secs." % (func.__name__, t2 - t1))
        return result

    return wrapper
