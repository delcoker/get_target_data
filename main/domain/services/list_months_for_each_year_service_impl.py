from .interfaces.list_months_for_each_year_service import ListMonthsForEachYearService
from dateutil.relativedelta import relativedelta
import pandas as pd


class ListMonthsForEachYearServiceImpl(ListMonthsForEachYearService):
    def list_months_for_each_year(dataset):
        copy_of_dataset = dataset.copy()
        copy_of_dataset['Close Month'] = copy_of_dataset['Close Date'].dt.strftime('%m-%Y')
        copy_of_dataset = copy_of_dataset.sort_values(['Close Month'])
        copy_of_dataset['Close Month'] = pd.to_datetime(copy_of_dataset['Close Month'])
        last_month = (copy_of_dataset['Close Month'].iat[-1])
        first_month_year = last_month.year - 1
        year_month_list = list()
        first_month_year = pd.to_datetime(first_month_year, format='%Y')
        for i in range(0, 24):
            date = pd.to_datetime(first_month_year) + relativedelta(months=+i)
            year_month_list.append([date])
        final_year_month_list = pd.DataFrame(year_month_list)
        final_year_month_list.columns = ['Date']
        final_year_month_list['Month'] = final_year_month_list['Date'].dt.month
        final_year_month_list['Year'] = final_year_month_list['Date'].dt.year

        return final_year_month_list
