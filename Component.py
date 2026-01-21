# Component class

import math
import numpy as np
import pandas as pd

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



components = [
        Component('CPU_core_0', 2.0, 2.0, 15.0, ['L1_cache_0']),
        Component('CPU_core_1', 2.0, 2.0, 15.0, ['L1_cache_1']),
        Component('L1_cache_0', 1.0, 1.0, 2.0, ['L2_cache']),
        Component('L1_cache_1', 1.0, 1.0, 2.0, ['L2_cache']),
        Component('L2_cache', 2.5, 2.5, 5.0, ['memory_ctrl']),
        Component('GPU_core', 3.0, 3.0, 25.0, ['L2_cache']),  # Shares L2
        Component('memory_ctrl', 2.0, 1.5, 8.0, ['IO_block']),
        Component('IO_block', 1.5, 2.0, 4.0, []),


# # ✅ HIGHLY STANDARD (99% of chips)
# standard_connections = {
#     'CPU → L1 cache': 'Always - each CPU has private L1',
#     'L1 → L2': 'Always - cache hierarchy is fundamental',
#     'Cache → Memory Controller': 'Always - need memory access',
#     'Memory Controller → IO': 'Almost always - IO needs memory',
# }

# # ⚠️ ARCHITECTURE-DEPENDENT (varies by design)
# variable_connections = {
#     'CPU ↔ GPU': 'NOT standard - depends on architecture',
#     'GPU → Cache': 'Varies - some share L2, some have separate cache',
#     'CPU → IO direct': 'Rare - usually goes through controller',
#     'Multiple CPUs': 'Can share L2 or have separate L2s',
# }

# # ❌ ALMOST NEVER
# rare_connections = {
#     'CPU → DRAM directly': 'No - always through memory controller',
#     'GPU → L1 cache': 'No - L1 is CPU-private',
#     'IO → Cache directly': 'Rare - usually through memory controller'
# }





# class ChipArchitectureBuilder:
#     """
#     Helper to build realistic chip architectures
#     """
    
#     def __init__(self, chip_type='general_purpose'):
#         self.chip_type = chip_type
#         self.components = []
#         self.connections = {}
    
#     def build_cache_hierarchy(self):
#         """Standard cache hierarchy (ALWAYS include this)"""
#         rules = {
#             'CPU_core': 'MUST connect to L1_cache',
#             'L1_cache': 'MUST connect to L2_cache or memory_ctrl',
#             'L2_cache': 'MUST connect to L3_cache or memory_ctrl',
#         }
        
#         # Example for 2 CPUs with shared L2
#         self.connections['CPU_core_0'] = ['L1_cache_0']
#         self.connections['CPU_core_1'] = ['L1_cache_1']
#         self.connections['L1_cache_0'] = ['L2_cache']
#         self.connections['L1_cache_1'] = ['L2_cache']
#         self.connections['L2_cache'] = ['memory_ctrl']
    
#     def add_gpu_connections(self, shares_cache=True):
#         """Add GPU - connection depends on architecture"""
#         if shares_cache:
#             # Modern integrated GPU (Intel, Apple, AMD APU)
#             self.connections['GPU_core'] = ['L2_cache', 'memory_ctrl']
#         else:
#             # Discrete GPU or separate cache
#             self.connections['GPU_core'] = ['GPU_L2_cache']
#             self.connections['GPU_L2_cache'] = ['memory_ctrl']
    
#     def add_io_connections(self):
#         """IO connections (standard pattern)"""
#         self.connections['memory_ctrl'] = ['IO_block']
#         self.connections['IO_block'] = []  # Endpoint
    
#     def get_architecture_template(self, arch_type):
#         """Get standard templates"""
#         templates = {
#             'simple_cpu': {
#                 # Minimal chip: 1 CPU, cache, memory, IO
#                 'CPU_core_0': ['L1_cache'],
#                 'L1_cache': ['L2_cache'],
#                 'L2_cache': ['memory_ctrl'],
#                 'memory_ctrl': ['IO_block']
#             },
            
#             'dual_core_cpu': {
#                 # 2 CPUs sharing L2
#                 'CPU_core_0': ['L1_cache_0'],
#                 'CPU_core_1': ['L1_cache_1'],
#                 'L1_cache_0': ['L2_cache'],
#                 'L1_cache_1': ['L2_cache'],
#                 'L2_cache': ['memory_ctrl'],
#                 'memory_ctrl': ['IO_block']
#             },
            
#             'cpu_gpu_integrated': {
#                 # CPU + GPU sharing resources
#                 'CPU_core_0': ['L1_cache_0'],
#                 'CPU_core_1': ['L1_cache_1'],
#                 'L1_cache_0': ['L2_cache'],
#                 'L1_cache_1': ['L2_cache'],
#                 'GPU_core': ['L2_cache'],  # Shares L2 with CPU
#                 'L2_cache': ['memory_ctrl'],
#                 'memory_ctrl': ['IO_block']
#             },
            
#             'high_performance_soc': {
#                 # Modern SoC with fabric
#                 'CPU_core_0': ['L1_cache_0'],
#                 'L1_cache_0': ['L2_cache_cpu'],
#                 'CPU_core_1': ['L1_cache_1'],
#                 'L1_cache_1': ['L2_cache_cpu'],
#                 'GPU_core': ['L2_cache_gpu'],
#                 'L2_cache_cpu': ['fabric'],
#                 'L2_cache_gpu': ['fabric'],
#                 'fabric': ['L3_cache', 'memory_ctrl'],
#                 'memory_ctrl': ['IO_block']
#             }
#         }
        
#         return templates.get(arch_type, templates['simple_cpu'])