import random
import numpy as np

def random_vector():
    return np.array([random.random(), random.random()])

def get_config():
    pass
    # TODO gets JSON config for PSO parameters? i.e. C0, C1, C2, fac and push?