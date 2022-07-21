from main.domain.services.interfaces.linear_model_calculation_service import LinearModelCalculationService
from main.domain.services.cmodel.create_new_column_in_data_frame_service_impl import CreateNewColumnInDataFrameServiceImpl
import numpy as np
from sklearn import linear_model
from sklearn.linear_model import LinearRegression

class LinearModelCalculationServiceImpl(LinearModelCalculationService):
    def implement_linear_model_calculation(dataset, all_products):
        copy_of_dataset = dataset.copy()
        copy_of_dataset = copy_of_dataset[['Close Month', 'Product Name', 'ARR']]
        copy_of_dataset['time'] = np.arange(len(copy_of_dataset.index))
        product_linear_data = []
        for product in all_products:
            product_values = {}
            filtered_data = copy_of_dataset[copy_of_dataset['Product Name'] == product]
            time_column_added_to_filtered_time = CreateNewColumnInDataFrameServiceImpl.create_time_column(filtered_data)
            x = time_column_added_to_filtered_time.time.values.reshape(-1, 1)
            y = time_column_added_to_filtered_time['ARR'].values
            model = linear_model.LinearRegression().fit(x, y)
            linear_model.LinearRegression(copy_X=True, fit_intercept=True, n_jobs=1, normalize=False)
            product_values['Product Name'] = product
            product_values['values'] = model.predict([[1], [2], [3], [4], [5], [6], [7], [8], [9], [10], [11], [12]])
            product_linear_data.append(product_values)
        return product_linear_data


