from .interfaces.calculate_mean_service import CalculateMeanService


class CalculateMeanServiceImpl(CalculateMeanService):
    def calculate_mean(dataset):
        mean_calculated = dataset.copy()
        mean_calculated = mean_calculated.groupby(["Month", "Product Name"])['ARR'].mean().reset_index(name='Mean_ARR')

        return mean_calculated

    def calculate_overall_mean_for_each_product(dataset):
        dataset_copy = dataset.copy()
        overall_mean_calculated = dataset_copy.groupby(['Product Name'])['ARR'].median().reset_index(
            name='Mean')
        return overall_mean_calculated
