import bar
import numpy as np
from time import sleep

min = 0
max = 100
step = 1
for i in np.arange(min, max,step): 
    bar1 = bar.drawGraph("Loading...", "%", i, min,max,color="green", numTicks=10, center=True)
    sleep(.01)
    for i in np.arange(min, max,step): 
        bar2 = bar.drawGraph("Processing...", "%", i, min,max,color="blue", numTicks=10, center=True)

        print('\033c')
        print(bar1 + "\n")
        print(bar2)
