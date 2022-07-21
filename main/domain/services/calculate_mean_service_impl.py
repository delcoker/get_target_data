from main.domain.services.interfaces.calculate_mean_service import CalculateMeanService


class CalculateMeanServiceImpl(CalculateMeanService):
    def calculate_mean(dataset):
        mean_calculated = dataset.copy()
        mean_calculated = mean_calculated.groupby(["Month", "Product Name"])['ARR'].mean().reset_index(name='Mean_ARR')

        return mean_calculated
