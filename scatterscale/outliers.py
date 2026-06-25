import numpy as np

def handle_outliers(data, sigma_value=10, treatment='mask_out', verbose=False):
    """
    Function to identify and handle outlier values in the distribution, which would drastically change the scaling of the colorbar if not addressed.

    Args
        data (1d float array): data to be represented by the colorbar.
        sigma_value (int, default 10): number of stddev to use when identifying outliers, if using the sigma method.
        treatment (str, default='mask_out'): how to treat the identified outliers; options are 'reassign' and 'mask_out'.
        verbose (bool, default=False): whether to display the number of outliers identified.
    
    Returns
        data_modified (1d float array): data to be represented by the colorbar, treated for outliers according to the specifications.
    """

    assert type(data) is np.ndarray, 'Input data must be a numpy array.'
        
    median = np.median(data)
    # center the gaussian at the median of the distribution
    stddev = np.std(data, mean=median)

    lower_bound = median - sigma_value * stddev
    upper_bound = median + sigma_value * stddev

    upper_outliers =  data > upper_bound
    lower_outliers =  data < lower_bound

    # make a deep copy
    data_modified = np.copy(data)

    # choose the method to treat outliers

    if treatment == 'mask_out':

        data_modified[upper_outliers | lower_outliers] = np.nan

    elif treatment == 'reassign':

        data_modified[upper_outliers] = upper_bound
        data_modified[lower_outliers] = lower_bound

    if verbose:
        print(f'{np.sum(upper_outliers)} upper outliers found.')
        print(f'{np.sum(lower_outliers)} lower outliers found.')

    return data_modified