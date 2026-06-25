# ScatterScale
Automate the normalizing scale for your scatterplot's colorbar. Scaling options are Log, SymLog, Asinh, or no normalization, as defined by [matplotlib](https://matplotlib.org/stable/api/colors_api.html#color-norms).

### To Install
```pip install scatterscale```

### Quick Start
Scatterscale's ```get_scatterscale()``` function can be used to generate the matplotlib.color.Norm used for matplotlib plotting.

```import scatterscale 
optimal_norm = get_scatterscale(data_for_colorbar)
plt.scatter(x_data, y_data, c=data_for_colorbar, norm=optimal_norm)
plt.show()
```

If you'd like to remove outliers from your data first, you can do so with ```handle_outliers()``` before running ```get_scatterscale()```.

```data_for_colorbar_no_outliers = handle_outliers(data_for_colorbar, sigma_value=5, treatment="mask_out")
optimal_norm_no_outliers = get_scatterscale(data_for_colorbar)
plt.scatter(x_data, y_data, c=data_for_colorbar_no_outliers, norm=optimal_norm_no_outliers)
plt.show()
```