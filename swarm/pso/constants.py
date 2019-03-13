import numpy as np

from pso.data import PSOData
from pso.util import get_config

class Const:
    # Assume constriction factor M = 1
    C0 = 1
    C1 = 0.5
    C2 = 0.5


'''
    # May not need in implimentation
    def update_parameters(self):
        pass
        # TODO Need to read in fac, push
        Const.C0 = (0.5-0.5*np.tanh(PSOData.cur_history_idx*Const.fac-Const.push))
        # Where fac = t2/stepdown and push = t2 + tpush from old code
'''