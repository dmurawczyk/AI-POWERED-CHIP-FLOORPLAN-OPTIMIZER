# Component class

import math
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.preprocessing import StandardScaler 

# are conenctins standard between components
class Component:
    def init(self, name, length, width, power, connections):
        # upper left
        self.x = 0
        self.y = 0
        self.name = name
        self.power = power
        self.length = length
        self.width = width
        self.connections = connections 
    def area(self):
        return self.width * self.length
    def corners(self):
        # upper left, upper right, lower left, lower right
        return [(self.x, self.y), (self.x+self.width, self.y), (self.x, self.y + self.length), (self.x + self.width, self.y + self.length)]


