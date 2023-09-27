"""All data analysis functions go here."""
import numpy as np
from scipy.optimize import curve_fit
from uncertainties import ufloat

def auto_lsq_fit(func, datax, datay, p_0 = None):
    """A fire-and-forget function to fit any data to any function.
        Produces a list of fit parameters, the fit function, the residual,
        and the reduced chi square value.
    
    Args:
        func (function): The function to fit to the data.
        datax (array): The x data.
        datay (array): The y data.
        P0 (array): The initial guess for the parameters.

    Returns:
        fit_params (list): The parameters of the fit.
    """
    fit = curve_fit(f=func, xdata=datax, ydata=datay, p0=p_0)

    params, cov, *_ = fit

    fit_params = [ufloat(param, np.sqrt(cov[i][i])) for i, param in enumerate(params)]

    func_args = tuple([datax]) + tuple(params)
    func_fit = func(*func_args)

    residual = datay - func_fit

    def result_func(x):
        return func(x, *params)

    chi_sq = np.sum((residual/func_fit)**2)/(len(datay) - len(params))

    return fit_params, result_func, residual, chi_sq
