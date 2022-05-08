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
from sktime.forecasting.theta import ThetaForecaster
from sktime.forecasting.tbats import TBATS
from sktime.forecasting.bats import BATS
from sktime.forecasting.croston import Croston
from sktime.forecasting.ets import AutoETS
from sktime.forecasting.fbprophet import Prophet
from sktime.forecasting.hcrystalball import HCrystalBallForecaster
from sktime.forecasting.naive import NaiveForecaster
from sktime.forecasting.statsforecast import StatsForecastAutoARIMA
from sktime.performance_metrics.forecasting import mean_squared_error

from sktime.performance_metrics.forecasting import mean_squared_error
import math
from keras.preprocessing.sequence import TimeseriesGenerator
from keras.models import Sequential
from keras.layers import Dense
from keras.layers import LSTM
from sklearn.preprocessing import MinMaxScaler
from sklearn.metrics import mean_squared_error

from sklearn.metrics import mean_squared_error #均方误差
from sklearn.metrics import mean_absolute_error #平方绝对误差
from sklearn.metrics import r2_score # R square

from sktime.utils.plotting import plot_series