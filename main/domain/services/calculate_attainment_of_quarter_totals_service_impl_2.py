from .interfaces.calculate_attainment_of_quarter_totals_service import CalculateAttainmentOfQuarterTotalsService


class CalculateAttainmentOfQuarterTotalsServiceImpl2(CalculateAttainmentOfQuarterTotalsService):
    def calculate_attainment_of_quarter_totals(dataset):
        copy_of_dataset = dataset.copy()
        copy_of_dataset['ATT Quarter Total'] = copy_of_dataset['ARR'] / copy_of_dataset['Quarter Total']
        return copy_of_dataset
