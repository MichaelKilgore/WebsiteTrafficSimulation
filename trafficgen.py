#!/usr/bin/env python3

import sys
import urllib3
import random
import time
from time import sleep

url = sys.argv[1]
rps = int(sys.argv[2])
jitter = float(sys.argv[3])

print(url, rps, jitter)

if jitter < 0:
    jitter = 0.1
elif jitter > 1:
    jitter = 1.0

lowerRPS = rps * (1.0 - jitter)
upperRPS = rps * (1.0 + jitter)

while True:
  currentRPS = random.randint(lowerRPS, upperRPS)
  start = time.time() 
  for i in range(currentRPS):
    http = urllib3.PoolManager()
    responseType = random.randint(0, 2)
    if responseType == 0:
      http.request('GET', url)
    if responseType == 1:
      http.request('GET', url + 'fail')
    else:
      http.request('GET', url + '404')
  end = time.time()
  if(1-(end-start)) > 0:
    sleep(1-(end-start))
  else:
    continue

