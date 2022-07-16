from .interfaces.extract_data_service import ExtractDataService
import datetime as dt


class ExtractDataBasedOnNumberOfYearsServiceImpl(ExtractDataService):
    def extract_data_based_on_number_of_years(dataset):
        number_of_years_of_data = 2
        current_year = dt.date.today().year
        copy_of_dataset = dataset.copy()
        copy_of_dataset = copy_of_dataset[(copy_of_dataset["Close Date"].dt.year >= (current_year - number_of_years_of_data)) & \
                                          (copy_of_dataset["Close Date"].dt.year < (current_year))]
        return copy_of_dataset
