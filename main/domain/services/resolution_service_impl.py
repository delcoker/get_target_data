from .interfaces.resolution_service import ResolutionService
from main.domain.services.calculate_mean_service_impl import CalculateMeanServiceImpl
import math

class ResolutionServiceImpl(ResolutionService):
    def anomaly_resolution(dataset):
        dataset_copy = dataset.copy()
        overall_means_for_each_product = CalculateMeanServiceImpl.calculate_overall_mean_for_each_product(dataset)
        for i, row in dataset_copy.iterrows():
            if math.isnan(row['ARR']) or row['ARR'] == 0:
                get_mean_row = overall_means_for_each_product.loc[
                    overall_means_for_each_product['Product Name'] == row['Product Name']]
                dataset_copy.at[i, 'ARR'] = round(get_mean_row['Mean'].values[0], 2)
        return dataset_copy
