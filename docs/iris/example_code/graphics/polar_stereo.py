import iris
filename = iris.sample_data_path('uk_hires.pp')
cubes = iris.load(filename)
print cubes 


import matplotlib.pyplot as plt

import iris
import iris.quickplot as qplt

fname = iris.sample_data_path('air_temp.pp')
temperature_cube = iris.load_cube(fname)

qplt.contourf(temperature_cube, 25)

plt.gca().coastlines()

plt.show()

