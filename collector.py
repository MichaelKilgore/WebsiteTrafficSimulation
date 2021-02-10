#!/usr/bin/env python3

import sys
import urllib.request
import time
from time import sleep

url = sys.argv[1] + 'stats'

interval = 10.0
for num, val in enumerate(sys.argv, start=1):
  if num == len(sys.argv):
    break
  if val == '--interval':
    interval = float(sys.argv[num])

while True:
  start = time.time()
  http = urllib.request.urlopen(url)
  line = str(http.read())
  #stats[time, 500s, 200s, 404s]
  stats = line.split("\\n")
  stats[0], stats[1], stats[2], stats[3] = (stats[0].replace("b'time: ", ""),
                                            stats[1].replace("500s: ", ""),
                                            stats[2].replace("200s: ", ""),
                                            stats[3].replace("404s: ", ""))
  with open('output.tsv', 'a') as f:
    f.write('\t'.join(stats[0:4]) + '\n')
  end = time.time()
  if(10-(end-start)) > 0:
    sleep(10-(end-start))
  else:
    continue
