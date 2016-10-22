from scipy.spatial import Voronoi, voronoi_plot_2d, KDTree
import numpy as np

# array of centers of sites of interest - read out of table in db
points = np.array([[0, 0], [0, 1], [0, 2], [1, 0], [1, 1], [1, 2],[2, 0], [2, 1], [2, 2],[1.5,1.5]]) 

# library that creates a map between point in x-y space and nearest site
tree = KDTree(points)

# returns index of site in above array that is closest to x-y point
print tree.query([.1, .1])[1]