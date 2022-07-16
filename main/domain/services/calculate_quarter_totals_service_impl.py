from .interfaces.calculate_quarter_totals_service import CalculateQuarterTotalsService


class CalculateQuarterTotalsServiceImpl(CalculateQuarterTotalsService):
    def calculate_quarter_totals(dataset):
        copy_of_dataset = dataset.copy()
        quarter_totals = copy_of_dataset.groupby(['Quarter', 'Year', 'Product Name'])['ARR'].sum().reset_index().rename({'ARR': 'Quarter Total'}, axis=1)
        return quarter_totals
