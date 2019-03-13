import random

class Bounds:
    # Bounds
    begin_x = 0
    begin_y = 0
    end_x = 0
    end_y = 0

    width_x = end_x - begin_x
    width_y = end_y - begin_y

    # PSO bin data
    bin_size = 10
    bin_number = (width_x * width_y) / (bin_size * bin_size)

    @staticmethod
    def random_point():
        return random.randint(0, Bounds.bin_number - 1)

    @staticmethod
    def coords_to_bin(coords):
        dx = coords.x - Bounds.begin_x
        dy = coords.y - Bounds.begin_y
        # TODO fuck your explanation, LMAO