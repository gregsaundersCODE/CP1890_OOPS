import time


def timer(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        func()
        end = time.time()


timer()
