import redis
import os
import traceback

if __name__ == '__main__':
    try:
        r = redis.Redis(
            host=os.getenv('REDIS_HOST'), 
            port=os.getenv('REDIS_PORT'), 
            db=0, 
            password=os.getenv('REDIS_PASS')
        )
        r.set('mykey1', 'so_original')
        print(f"Key: mykey1, value: {r.get('mykey1')}")
        print("Hello world")
    except Exception as e:
        traceback.print_exc()
        raise e
