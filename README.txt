# WebsiteMonitoring

first I ran the CS390 Time Server file on the csslab1 linux lab computer
then I ran the "trafficgen.py" file with command
"./trafficgen.py http://csslab1:8080/ 500 0.5"
then I ran
"./collector.py http://csslab1:8080/"
And I let both of the files run for an hour thus created my "output.tsv" file
Then I ran
"./plot.py"
This created my "graph.png"

