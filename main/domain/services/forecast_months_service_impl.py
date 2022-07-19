from .interfaces.forecast_months_service import ForecastMonthsService
import datetime as dt
from dateutil.relativedelta import relativedelta
import pandas as pd

class ForecastMonthsServiceImpl(ForecastMonthsService):
    def __init__(self):
        pass

    def list_months_for_forecasted_year(self, dataset):
        last_month = (dataset['Date'].iat[-1])

        last_month = str(last_month.month) + '-' + str(last_month.year)
        last_month = dt.datetime.strptime(last_month, "%m-%Y")

        forecast_months_list = list()
        for i in range(1, 13):
            date = last_month + relativedelta(months=+i)
            forecast_months_list.append([date])

        forecast_months = pd.DataFrame(forecast_months_list)
        forecast_months.columns = ['Forecast Month']
        forecast_months['Month'] = forecast_months['Forecast Month'].dt.month
        forecast_months['Year'] = forecast_months['Forecast Month'].dt.year
        return forecast_months
