from main.domain.services.interfaces.extract_data_service import FilterDataService

import datetime as dt


class FilterDataByYearServiceImpl(FilterDataService):
    def __init__(self):
        pass

    def extract_data_based_on_number_of_years(self, dataset):
        number_of_years_of_data = 2
        current_year = dt.date.today().year
        copy_of_dataset = dataset.copy()
        copy_of_dataset = copy_of_dataset[(copy_of_dataset["Close Date"].dt.year >= (current_year - number_of_years_of_data)) & \
                                          (copy_of_dataset["Close Date"].dt.year < current_year)]
        return copy_of_dataset
