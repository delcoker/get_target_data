from main.domain.services.interfaces.forecast_months_service import ForecastMonthsService
from main.domain.services.interfaces.modelling_technique_strategy_service import ModellingTechniqueStrategyService
from main.domain.services.cmodel.extract_closed_won_data_service_impl import FilterClosedWonDataService
from main.domain.services.cmodel.list_months_for_each_year_service_impl import ListMonthsForEachYearServiceImpl
from main.domain.services.merge_data_service_impl import MergeDataServiceImpl
from main.domain.services.cmodel.get_monthly_revenue_for_products_service_impl import GetMonthlyRevenueForProductsService
from main.domain.services.resolution_service_impl import ResolutionServiceImpl
from main.domain.services.cmodel.create_new_column_in_data_frame_service_impl import CreateNewColumnInDataFrameServiceImpl
from main.domain.services.linear.linear_model_calculation_service_impl import LinearModelCalculationServiceImpl


class LinearModelServiceImpl(ModellingTechniqueStrategyService):

    def __init__(self, forecast_months_service: ForecastMonthsService):
        self.forecast_months_service = forecast_months_service

    def evaluate_model(self, filtered_data, all_products, fe_product_growth):
        closed_won_filtered_data = FilterClosedWonDataService.extract_closed_won_data(filtered_data)
        listed_months_for_each_year = ListMonthsForEachYearServiceImpl.list_months_for_each_year(filtered_data)
        listed_products_for_each_month_for_each_year = MergeDataServiceImpl.merge_products_with_each_month_for_each_year(
            listed_months_for_each_year, all_products)
        monthly_totals_for_products = GetMonthlyRevenueForProductsService.get_monthly_revenue_for_products(
            closed_won_filtered_data)
        merged_monthly_totals_with_listed_products = MergeDataServiceImpl.merge_monthly_totals_with_listed_products(
            listed_products_for_each_month_for_each_year, monthly_totals_for_products)
        merged_monthly_totals_with_listed_products = ResolutionServiceImpl.anomaly_resolution(
            merged_monthly_totals_with_listed_products)
        add_close_month_column = CreateNewColumnInDataFrameServiceImpl.create_close_month_column(merged_monthly_totals_with_listed_products)
        linear_data_for_each_product = LinearModelCalculationServiceImpl.implement_linear_model_calculation(add_close_month_column, all_products)
        # print(linear_data_for_each_product)
        return linear_data_for_each_product
        # return {'linear': 'linear'}
