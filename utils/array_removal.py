import numpy as np

def remove_array(big_list, small_list):
    return big_list[~np.isin(big_list, small_list)]