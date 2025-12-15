this is our ai powered chip designer
input (components): CPU core 0, CPU core 1, L1 cache, L2 cache, GPU, memory_ctrl, IO_block
output (schematic): optimize cost based on thermal hotspots, chip area, and wire congestion -- equation: cost = wirelength + 2*power density + .5*chip area
class1: component (bare minimum-at least one CPU core, cache, IO_block, memory_ctrl, and GPU core) 
class2: chip 
class3: optimimum chip
class4: neural network
class5: draw
for class1: initialize variable, its connections, its characteristics (x,y, connection names, power/heat per component)
for class2: dimensions of chip, list of components, add_connection (insert tuple of components connected), generate_random_placement(given all components and connections just place randomly on chip)
for class3: generate_training_data(calls random_placement many times and outputs cost)
for class4: build model using relu and tanh, train it, predict cost 
for class5: given mimimal cost, generate a diagram of the placement of each component and its connections