import numpy as np

# PSO Data
class PSOData:

    def __init__(self):
        # Location / reading history
        self.location_history = []
        self.reading_history = []
        self.cur_history_idx = -1

        # Local / global best
        self.global_best_reading = Reading(0)
        self.local_best_reading = Reading(0)
        self.global_best_coords = np.array([0, 0])
        self.local_best_coords = np.array([0, 0])

      
    def add_point(self, coords, reading):
        self.location_history.append(coords)
        self.reading_history.append(reading)
        # Could maybe separate into separate function/method?
        if self.local_best_reading.should_update_to(reading):
            self.local_best_reading = reading
        if self.global_best_reading.should_update_to(reading):
            self.global_best_reading = reading
             
        self.cur_history_idx += 1


# Simple coordinate wrapper
class Coordinates:

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def vec(self):
        return np.array([self.x, self.y])


# Simple reading wrapper
class Reading:

    def __init__(self, value):
        # TODO : default None and ternary check if self.value is nothing
        self.value = value

    def should_update_to(self, other_reading):
        return other_reading.value > self.value