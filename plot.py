#!/usr/bin/env python3

import matplotlib.pyplot as plt

with open('output.tsv', 'r') as f:
  lines = f.readlines()
  
times, s500, s200, s404  = [], [], [], []
s500YPoints, s200YPoints, s404YPoints = [], [], []

for i, line in enumerate(lines):
  line = lines[i].split('\t')
  s500.append(int(line[1]))
  s200.append(int(line[2]))
  s404.append(int(line[3]))
  if i % 6 == 0 and i > 5:
    times.append(int(line[0]))

    rps = s500[-1] - s500[0]
    s500YPoints.append(rps)

    rps = s200[-1] - s200[0]
    s200YPoints.append(rps)

    rps = s404[-1] - s404[0]
    s404YPoints.append(rps)

    s500, s200, s404 = [], [], []

plt.scatter(times,s500YPoints)
plt.plot(times,s500YPoints)
plt.plot(times,s200YPoints)
plt.plot(times,s404YPoints)
plt.title("Time Server Status")
plt.xlabel("Unix Time")
plt.ylabel("RPS (1-minute rate)")
plt.legend(['s500', 's200', 's404'])
plt.savefig('graph.png')
  

 


