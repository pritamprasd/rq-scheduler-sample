from time import time, sleep

def sample_job(t: float):
    print(f"Job started: {time()}")
    sleep(t)
    print(f"Job ended: {time()}")