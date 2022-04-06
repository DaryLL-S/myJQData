"""
@author: DaryLS
@software: PyCharm
@file: sktime_test.py
@create_time: 2022-04-04 08:39
@edit_time: 2022/4/4 8:39
"""
data = "new_data/data_set.csv"
import matplotlib.dates as mdate
from sktime.forecasting.exp_smoothing import ExponentialSmoothing
from sktime.forecasting.theta import ThetaForecaster
from sktime.forecasting.arima import AutoARIMA