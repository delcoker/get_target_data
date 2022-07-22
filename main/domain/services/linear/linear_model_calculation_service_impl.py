import numpy as np
import pandas as pd
# from sklearn import linear_model
#
# from main.domain.services.cmodel.create_new_column_in_data_frame_service_impl import CreateNewColumnInDataFrameServiceImpl
# from main.domain.services.forecast_months_service_impl import ForecastMonthsServiceImpl
from main.domain.services.interfaces.linear_model_calculation_service import LinearModelCalculationService


class LinearModelCalculationServiceImpl(LinearModelCalculationService):
    def implement_linear_model_calculation(dataset, all_products):
        # copy_of_dataset = dataset.copy()
        # copy_of_dataset = copy_of_dataset[['Close Month', 'Product Name', 'ARR']]
        # copy_of_dataset['time'] = np.arange(len(copy_of_dataset.index))
        # product_linear_data = pd.DataFrame()
        # forecast_months_service = ForecastMonthsServiceImpl()
        # forecast_months = forecast_months_service.list_months_for_forecasted_year(dataset)
        #
        # for product in all_products:
        #     forecast_months_copy = forecast_months
        #     filtered_data = copy_of_dataset[copy_of_dataset['Product Name'] == product]
        #     time_column_added_to_filtered_time = CreateNewColumnInDataFrameServiceImpl.create_time_column(filtered_data)
        #     x = time_column_added_to_filtered_time.time.values.reshape(-1, 1)
        #     y = time_column_added_to_filtered_time['ARR'].values
        #     model = linear_model.LinearRegression().fit(x, y)
        #     linear_model.LinearRegression(copy_X=True, fit_intercept=True, n_jobs=1, normalize=False)
        #     product_predictions = model.predict([[1], [2], [3], [4], [5], [6], [7], [8], [9], [10], [11], [12]])
        #     forecast_months_copy['Product Name'] = product
        #     forecast_months_copy['linear_model'] = product_predictions
        #     product_linear_data = pd.concat([product_linear_data, forecast_months_copy])
        # product_linear_data['linear_model'].round(decimals=2)
        # product_linear_data = product_linear_data.reset_index(drop=True)
        # return product_linear_data
        pass
