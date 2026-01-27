# Chip class

import math
import random
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.preprocessing import StandardScaler 

class Chip:
    def __init__(self, length, width):
        self.length = length
        self.width = width
        self.totalPower = 0
        self.components = []
        self.connections = {}
        self.wirelength = 0
    
    def addComponent(self, c : Component):
        self.totalPower += c.power()
        self.components.append(c)
    
    def addConnections(self, con, con2):
        if con not in self.connections:
            self.connections[con] = []
        self.connections[con].append(con2) 

    def generateRandomPlacement(self):
        #create each row of our training data
        
        if self.componenents == [] and self.connections == []:
            self.components = [
                Component('CPU_core_0', 2.0, 2.0, 15.0, ['L1_cache_0']),
                Component('CPU_core_1', 2.0, 2.0, 15.0, ['L1_cache_1']),
                Component('L1_cache_0', 1.0, 1.0, 2.0, ['L2_cache']),
                Component('L1_cache_1', 1.0, 1.0, 2.0, ['L2_cache']),
                Component('L2_cache', 2.5, 2.5, 5.0, ['memory_ctrl']),
                Component('GPU_core', 3.0, 3.0, 25.0, ['L2_cache']),  # Shares L2
                Component('memory_ctrl', 2.0, 1.5, 8.0, ['IO_block']),
                Component('IO_block', 1.5, 2.0, 4.0, []),
            ]
            # if orientation needs to be changed, change attribute of componenet ('v'->'h')
        n = len(components)
        area = (chip.width)*(chip.length)/n
        rows = math.ceil(math.sqrt(n))
        cols = math.ceil(n/rows)
        region_h = chip.length/rows
        region_w = chip.width/cols
        parts = []

        for i in self.components:
            parts.append(i)

        columns = [0]*cols
        grid = columns*rows

        for component in self.components:
            component.orientation = random.choice(['v', 'h'])
            component.order = random.choice()
            # default
            if component.orientation == 'v':
                new_width = component.width
                new_height = component.height
            # flip dimensions
            if component.orientation == 'h':
                new_width = component.height
                new_height = component.width
        
        for i in range(cols):
            for j in range(rows):
                label = random.choice(parts)
                grid[i][j]= label
                parts.remove(label)



        #range of occupied
        #generate visual layout
        for i in self.components:
            # place each one 
    
    def network(self):
        # input: chip dimensions, cost per datapoint 

    def wirelength(self, c : Component, c2 : Component):
        # assuming vertical orientation
        center_c = (c.x + c.width/2, c.y + c.height/2)
        center_c2 = (c2.x + c2.width/2, c2.y + c2.height/2)
        if c.orientation == 'h':
            center_c = (c.x + c.height/2, c.y + c.width/2)
        if c2.orientation == 'h':
            center_c2 = (c2.x + c2.height/2, c2.y + c2.width/2)
        return math.dist(center_c2, center_c)

    # each component has a power consumption feature and we want to avoid putting highly power consumptive componenets adjacent to each other
    def powerPercentage(self, c : Component):
        # normalizes power
        return (c.power() / self.totalPower) * 100   

    # how much of the area of the chip are we using
    def optimalArea(self):
#         CPU:   x + width  = 1.0 + 2.0 = 3.0
#         Cache: x + width  = 4.0 + 1.5 = 5.5 ← MAX
#         GPU:   x + width  = 2.0 + 2.2 = 4.2
#         max_x = 5.5
#         Calculate Max Y:
#         pythonCPU:   y + length = 1.0 + 2.0 = 3.0
#         Cache: y + length = 1.0 + 1.5 = 2.5
#         GPU:   y + length = 5.0 + 2.2 = 7.2 ← MAX
#         max_y = 7.2
#         Calculate Area:
#         pythonarea = max_x × max_y = 5.5 × 7.2 = ??

    
    def cost(self, wirelength, powerDensity. optimalArea):
        cost = wirelength + 2*power density + .5*chip area