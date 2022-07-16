from .interfaces.data_conversion_service import DataConversionService
import datetime as dt


class DataConversionServiceImpl(DataConversionService):
    def convert_month_name_to_number(month_name) -> dict:
        datetime_object = dt.datetime.strptime(month_name, "%B")
        month_number = datetime_object.month
        return month_number

    def convert_month_number_to_name(month_number) -> dict:
        if month_number == 0:
            month_number = 12
        datetime_object = dt.datetime.strptime(str(month_number), "%m")
        month_name = datetime_object.strftime("%b")
        return month_name
