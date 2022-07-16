from .interfaces.calculate_attainment_of_yearly_totals_service import CalculateAttainmentOfYearlyTotalsService


class CalculateAttainmentOfYearlyTotalsServiceImpl(CalculateAttainmentOfYearlyTotalsService):
    def calculate_attainment_of_yearly_totals(dataset):
        copy_of_dataset = dataset.copy()
        copy_of_dataset['ATT Year Total'] = copy_of_dataset['ARR'] / copy_of_dataset['Total Arr Yearly']
        return copy_of_dataset
