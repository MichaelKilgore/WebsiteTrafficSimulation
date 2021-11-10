Synopsis:

This program essentially simulates a website having traffic. The timeserver created by my instructor, is meant to be run on a server, this starts a website. The trafficgen is used to simulate pings sent to the website. Then the Collector periodically samples the server statistics. This was run for an hour, and all the data collected was thrown into the output.tsv file. Finally plot.py was used to plot all the data collected onto a graph in the graph.png.

This code can also be run on other websites to test stability of sites.


Usage:

first I ran the CS390 Time Server file on the csslab1 linux lab computer, then I ran the "trafficgen.py" file with command, "./trafficgen.py http://csslab1:8080/ 500 0.5", then I ran "./collector.py http://csslab1:8080/", And I let both of the files run for an hour thus creating my "output.tsv" file. Then I ran "./plot.py" which created my "graph.png".

You can use this project to test your own sites load capabilities. Just run the "./trafficgen.py URL 500 0.5". This will send a custom amount of traffic volume to your URL.
