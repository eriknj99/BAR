#!/usr/bin/python
import os
from time import sleep
from termcolor import colored
import numpy as np
import builtins
def drawGraph(lable, unit, val, min, max, color="white", precision=3, numTicks=10, center=False):
        
        # Eliminate overflow
        if(val > max):
            max = val

        # Translate min to 0 to make everything easier
        # Only the displayed data will be translated back
        val -= min
        max -= min

        tick = '┼'
        hLine = '─'
        vLine = '│'
        c0 = '├'
        c1 = '┤'
        c2 = '└'
        c3 = '┘'
        blocks = ["","▏","▎","▍","▌","▋","▊","▉","█"]
        blockSpace = ' '
        space = ' '
        
        output = ""

        rows_str, columns_str = os.popen('stty size', 'r').read().split()
        columns = int(columns_str)

        # Generate Lables
        tick_lables = []
        float_tick_lables = []
        len_tick_lables = 0
        for i in range(0,numTicks + 1):
            float_tick_lables.append(round((i * max/numTicks), precision))
            
            # Translate the lable strings back to the correct value
            tick_lables.append(f"{(float_tick_lables[i] + min):g}{unit}") 
            
            len_tick_lables += len(tick_lables[i]) 

        # Generate tick spacing strings  
        tick_spacing_size = int(((columns - len_tick_lables) / (numTicks)) + .4) 
        tick_space = hLine * tick_spacing_size
       
        len_tick_lable_line = 0
        for i in range(numTicks):
            len_tick_lable_line += len((tick_lables[i]) + space * (tick_spacing_size - (len(tick_lables[i]) -1)))
        
        # Generate spacing to center the graph
        if(center):
            centering_string = space * int((columns - len_tick_lable_line)/2)
        else:
            centering_string = ""

        #Move tick lable line to the center
        output += centering_string

        # Generate tick lable line 
        for i in range(numTicks):
                output+=(tick_lables[i]) + space * (tick_spacing_size - (len(tick_lables[i]) -1))
        output += tick_lables[numTicks] 
       
        #Generate tick line
        output += "\n" + centering_string # Center the new line
        output += c0 # Add the first tick char
        for i in range(numTicks):
            offset = len(tick_lables[i]) -1  # Account for the length of the tick lable  
            output += tick_space  
            # Only add a tick if it is not the last tick 
            if(i != numTicks-1):
                output += tick

        output += c1# Add the last tick char
       
        # Generate the data line
        output += "\n" + centering_string
        output += vLine # Add the beginning of the bar
        
        # The length of the usable section of the data line. Accounting for the start and end of the bar
        len_data_line = len_tick_lable_line -1        
        len_filled = 0
        ideal_block_len = (len_data_line+1) * (val/max) -1 

        output += colored(blocks[8], color) * int(ideal_block_len)
        len_filled += int(ideal_block_len)

        remainder = (ideal_block_len + .5 - int(ideal_block_len))
         
        if(remainder > 1):
            output += colored(blocks[8], color)
            remainder-=1
            len_filled += 1

        partial_block_index = 0
        if(ideal_block_len < len_data_line - 1):
            partial_block_index = builtins.max(0,int(remainder * 8))
            output += colored(blocks[partial_block_index], color)
            len_filled += len(blocks[partial_block_index])

        output += space * (len_data_line - len_filled)
        output += vLine

        # Add the bottom line
        output += "\n" + centering_string + c2 + (len_data_line*hLine) + c3
      
        # Add the info line
        output = f"{centering_string}{lable} {round((val + min), precision):g}{unit} \n" + output

        return output    


    
