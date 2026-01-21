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
    def powerDensity(self):

    # how much of the area of the chip are we using
    def optimalArea(self):
    
    def cost(self, wirelength, powerDensity. optimalArea):
        cost = wirelength + 2*power density + .5*chip area