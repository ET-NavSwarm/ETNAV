import numpy as np

from pso.data import PSOData, Reading
from pso.calc import calculate_next_location

def next_location_test():
    d = PSOData()
    d.add_point(np.array([3, 5]), Reading(4))
    d.add_point(np.array([2, 4]), Reading(5))
    d.global_best_reading = Reading(7)
    d.global_best_coords = np.array([6, 6])

    vec = calculate_next_location(d)
    print("X: {}, Y: {}".format(vec[0], vec[1]))
