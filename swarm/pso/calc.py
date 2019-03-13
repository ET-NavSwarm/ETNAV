import numpy as np
import pso.util
from pso.bounds import Bounds
from pso.constants import Const
from pso.data import PSOData

def calculate_next_location(data: PSOData):
    # No points taken yet - error
    if data.cur_history_idx == -1:
        print("No history added yet")
        return None
    # Calculate locations
    if data.cur_history_idx == 0:
        old_loc = np.round(Bounds.random_point() * pso.util.random_vector())
    else:
        old_loc = data.location_history[-2]
    cur_loc = data.location_history[-1]

    # Currrent velocity
    cur_d = cur_loc - old_loc

    r1 = pso.util.random_vector()
    r2 = pso.util.random_vector()

    next_d = (Const.C0 * cur_d) + \
              (Const.C1 * r1 * (data.local_best_coords - cur_loc)) + \
              (Const.C2 * r2 * (data.global_best_coords - cur_loc))

    return np.floor(cur_loc + next_d)