import redis
import os
import traceback

if __name__ == '__main__':
    try:
        redis.Redis(
            host=os.getenv('REDIS_HOST'), 
            port=os.getenv('REDIS_PORT'), 
            db=0, 
            password=os.getenv('REDIS_PASS')
        )
        print("Hello world")
    except Exception as e:
        traceback.print_exception()
        raise e
