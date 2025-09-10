import time
import os

var = os.getenv('SYSTEM_PROMPT', 'NOT PROVIDED!!!!!')

i = 1
while True:
    print(f"Running service {i}: {var}")
    time.sleep(3)
    i += 1
