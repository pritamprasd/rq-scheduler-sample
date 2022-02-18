from time import sleep
import redis
import os
import traceback
from rq import Queue
from sample_job import sample_job

if __name__ == '__main__':
    print("----------demo.py START-------------")
    try:
        r = redis.Redis(
            host=os.getenv('REDIS_HOST'), 
            port=os.getenv('REDIS_PORT'), 
            db=0, 
            # password=os.getenv('REDIS_PASS')
        )

        queue = Queue(connection=r)
        for _ in range(10):
            print(f"Sending new job....")
            queue.enqueue(sample_job, 10.0)
            sleep(2)
        print("----------END-------------")
    except Exception as e:
        traceback.print_exc()
        raise e