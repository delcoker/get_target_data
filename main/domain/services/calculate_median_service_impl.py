from .interfaces.calculate_median_service import CalculateMedianService


class CalculateMedianServiceImpl(CalculateMedianService):
    def calculate_median(dataset):
        median_calculated = dataset.copy()
        # ST3_merge_with_overall_data_copy = 
        median_calculated = median_calculated.groupby(["Month", "Quarter", "Product Name"])['ATT Year Total'].mean().reset_index(name='Median')
        return median_calculated
