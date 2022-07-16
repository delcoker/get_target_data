import pandas as pd

from main.domain.services.interfaces.data_etl_service import DataEtlService


# https://www.w3schools.com/python/python_classes.asp
class CleanDataServiceImpl(DataEtlService):
    def __init__(self):
        # self.data_to_clean = data_to_clean
        pass

    def standard_data_clean(self, data_to_clean):
        copy_of_data_to_clean = data_to_clean.copy()
        # Change probability values to decimals and if no data replace with 0
        # copy_of_data_to_clean['Probability'] = copy_of_data_to_clean['Probability'].apply(lambda x: int(x) / 100 if x.isnumeric() else 0)
        # Format date columns
        # copy_of_data_to_clean['Probability'] = copy_of_data_to_clean['Probability'].apply(lambda x: x.replace("%", ""))
        copy_of_data_to_clean['Probability'] = copy_of_data_to_clean['Probability'].str.replace('%', '')

        copy_of_data_to_clean['Probability'] = copy_of_data_to_clean['Probability'].apply(lambda x: int(x) / 100 if x.isnumeric() else 0)
        # copy_of_data_to_clean['Created Date'] = copy_of_data_to_clean['Created Date'].apply(lambda x: pd.to_datetime(x))
        copy_of_data_to_clean['Created Date'] = pd.to_datetime(copy_of_data_to_clean['Created Date'])

        # copy_of_data_to_clean['Close Date'] = copy_of_data_to_clean['Close Date'].apply(lambda x: pd.to_datetime(x))
        copy_of_data_to_clean['Close Date'] = pd.to_datetime(copy_of_data_to_clean['Close Date'])

        # copy_of_data_to_clean['Last Activity'] = copy_of_data_to_clean['Last Activity'].apply(lambda x: pd.to_datetime(x))
        copy_of_data_to_clean['Last Activity'] = pd.to_datetime(copy_of_data_to_clean['Last Activity'])

        # Format age column to be a number else replace with 0
        copy_of_data_to_clean['Age'] = copy_of_data_to_clean['Age'].apply(lambda x: int(x) if type(x) == int else 0)
        # Remove dollar signs and commas
        # copy_of_data_to_clean['ARR'] = copy_of_data_to_clean['ARR'].apply(lambda x: x.replace("$", "").replace(",", ""))
        copy_of_data_to_clean['ARR'] = copy_of_data_to_clean['ARR'].str.replace('$', '').str.replace(",", "")

        # Check ARR is a number else replace with 0
        # copy_of_data_to_clean['ARR'] = copy_of_data_to_clean['ARR'].apply(lambda x: x if x.isnumeric() else 0)
        copy_of_data_to_clean['ARR'] = pd.to_numeric(copy_of_data_to_clean['ARR'], errors='coerce')
        copy_of_data_to_clean['ARR'] = copy_of_data_to_clean['ARR'].fillna(0)

        # Make sure ARR is a float type
        copy_of_data_to_clean['ARR'] = copy_of_data_to_clean['ARR'].astype(float)
        return copy_of_data_to_clean
