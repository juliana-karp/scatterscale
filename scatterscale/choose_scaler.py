from scipy.stats import entropy
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import matplotlib.colors as colors


def get_scatterscale(data):
    """Optimal scaler

    Return the norm function corresponding to the visually-optimal data scaling. 
    Options are no normalization, Asinh, SymLog, and Log.

    Args:

        data (array): numpy vector. 1D data that the scaling is calculated for.

    Returns:

        matplotlib.colors.Norm: data normalization function
    """

    # These functions return a matplotlib.colors norm function that can be operated on data or directly
    # used as the norm for a colorbar.
    def no_norm_operator(data):
        return colors.Normalize(vmin=np.nanmin(data), vmax=np.nanmax(data))
    def asinh_norm_operator(data, linear_width=1):
        return colors.AsinhNorm(vmin=np.nanmin(data), vmax=np.nanmax(data), linear_width=linear_width)
    def log_norm_operator(data):
        return colors.LogNorm(vmin=np.nanmin(data), vmax=np.nanmax(data))
    def symlog_norm_operator(data, linthresh=0.1):
        return colors.SymLogNorm(vmin=np.nanmin(data), vmax=np.nanmax(data), linthresh=linthresh)
    
    all_scalings = [no_norm_operator, asinh_norm_operator, symlog_norm_operator, log_norm_operator]
    all_scaling_names = ["No normalization", "Asinh (linear_width=1)", "SymLog (linthresh=0.1)", "Log"]
    if not np.all(data > 0):
        all_scalings = all_scalings[:-1] # get rid of log scaling option for data that has values <= 0

    entropies = []
    for i, get_scaling_operator in enumerate(all_scalings):
        scaling_operator = get_scaling_operator(data)
        scaled_data = scaling_operator(data)

        if all_scaling_names[i] == "No normalization":
            # scale to a range of 0 to 1 so that entropy can be calculated (otherwise fails for negative values)
            scaled_data_min = np.min(scaled_data)
            scaled_data_max = np.max(scaled_data)
            reranged_scaled_data = (scaled_data - scaled_data_min) / (scaled_data_max - scaled_data_min)
            entropies.append(entropy(reranged_scaled_data))
        else:
            entropies.append(entropy(scaled_data))

    # the distribution with max entropy has its values spread out the most evenly over the range
    loc_max_entropy = np.argmax(entropies)
    get_best_scaling_operator = all_scalings[loc_max_entropy]
    print(f"Best scaling: {all_scaling_names[loc_max_entropy]}")
    return get_best_scaling_operator(data)