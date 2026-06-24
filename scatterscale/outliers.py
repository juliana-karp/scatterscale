import numpy as np

def handle_outliers(dist, sigma_value=10, treatment='reassign'):
    """
    Function to identify and handle outlier values in the distribution,
    which would drastically change the scaling of the colorbar if not addressed.

    Inputs
    -------
    dist: 1d float array
        data to be represented by the colorbar.
    sigma_value: int, default 10
        number of stddev to use when identifying outliers, if using the sigma method.
    treatment: str, default='reassign'
        how to treat the identified outliers. options are 'reassign' and 'mask_out'.
    
    Outputs
    -------
    modified_dist: 1d float array
        data to be represented by the colorbar, treated for outliers according to the specifications.
    """
        
    median = np.median(dist)
    # center the gaussian at the median of the distribution
    stddev = np.std(dist, mean=median)

    lower_bound = median - sigma_value * stddev
    upper_bound = median + sigma_value * stddev

    upper_outliers =  dist > upper_bound
    lower_outliers =  dist < lower_bound

    # choose the method to treat outliers

    if treatment == 'reassign':

        # make a deep copy
        dist_modified = np.copy(dist)
        dist_modified[upper_outliers] = upper_bound
        dist_modified[lower_outliers] = lower_bound

    elif treatment == 'mask_out':

        dist_modified = dist[~upper_outliers & ~lower_outliers]

    return dist_modified