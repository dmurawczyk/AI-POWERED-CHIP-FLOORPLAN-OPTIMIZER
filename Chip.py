# Chip class

import math
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.preprocessing import StandardScaler 

class Chip:
    def init(self, length, width):
        self.length = length
        self.width = width
        self.components = []
        self.connections = {}
        self.wirelength = 0
    
    def addComponent(self, c : Component):
        self.components.append(c)
    
    def addConnections(self, con, con2):
        if con not in self.connections:
            self.connections[con] = []
        self.connections[con].append(con2) 

    def generateRandomPlacement(self):
        #range of occupied
        #generate visual layout
        for i in self.components:
            # place each one 

    def wirelength(self):

    # how does this work? is it between componenets or on compoenents
    each component has a pwoer consumption feature and we want to avoid putting highly power consumptive componenets adjacent to each other
    def powerDensity(self):

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
# ```

    
    def cost(self, wirelength, powerDensity. optimalArea):
        cost = wirelength + 2*power density + .5*chip area