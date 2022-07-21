from main.domain.services.interfaces.create_new_column_in_data_frame_service import CreateNewColumnInDataFrameService
from main.domain.services.data_conversion_service_impl import DataConversionServiceImpl
import pandas as pd
import calendar
import datetime as dt
import numpy as np


class CreateNewColumnInDataFrameServiceImpl(CreateNewColumnInDataFrameService):
    def create_quarter_column_in_dataset(dataset):
        copy_of_dataset = dataset.copy()
        fiscal_start_year = 'January'
        fiscal_start_year_number = DataConversionServiceImpl.convert_month_name_to_number(fiscal_start_year)
        fiscal_end_year = DataConversionServiceImpl.convert_month_number_to_name(fiscal_start_year_number - 1)
        freq = 'Q-' + fiscal_end_year.upper()

        copy_of_dataset['Quarter'] = pd.PeriodIndex(copy_of_dataset['Date'], freq=freq).strftime('Q%q')
        return copy_of_dataset

    def create_month_name_column(dataset):
        copy_of_dataset = dataset.copy()
        copy_of_dataset['Month_Name'] = copy_of_dataset['Month'].apply(lambda x: calendar.month_abbr[x])
        return copy_of_dataset

    def create_close_month_column(dataset):
        copy_of_dataset = dataset.copy()
        copy_of_dataset['Close Month'] = copy_of_dataset['Date'].dt.strftime('%m-%Y')
        return copy_of_dataset

    def create_time_column(dataset):
        copy_of_dataset = dataset.copy()
        copy_of_dataset['Time'] = np.arange(len(copy_of_dataset.index))
        return copy_of_dataset
