from main.domain.services.calculate_c_model_service_impl import CalculateCModelServiceImpl
from main.domain.services.calculate_mean_service_impl import CalculateMeanServiceImpl
from main.domain.services.calculate_median_service_impl import CalculateMedianServiceImpl
from main.domain.services.calculate_percentage_growth_service_impl import CalculatePercentageGrowthServiceImpl
from main.domain.services.calculate_quarter_totals_service_impl import CalculateQuarterTotalsServiceImpl
from main.domain.services.calculate_yearly_totals_for_each_product_service_impl import CalculateYearlyTotalsForEachProductServiceImpl
from main.domain.services.contexts.attainment_table_strategy_context_i import AttainmentTableStrategyContextI
from main.domain.services.create_new_column_in_data_frame_service_impl import CreateNewColumnInDataFrameServiceImpl
from main.domain.services.enums.attainment_table_type import AttainmentTableType
from main.domain.services.extract_closed_won_data_service_impl import ExtractClosedWonDataService
from main.domain.services.get_monthly_revenue_for_products_service_impl import GetMonthlyRevenueForProductsService
from main.domain.services.interfaces.forecast_months_service import ForecastMonthsService
from main.domain.services.interfaces.modelling_technique_strategy_service import ModellingTechniqueStrategyService
from main.domain.services.list_months_for_each_year_service_impl import ListMonthsForEachYearServiceImpl
from main.domain.services.merge_data_service_impl import MergeDataServiceImpl


class ExponentialModelServiceImpl(ModellingTechniqueStrategyService):

    def __init__(self, attainment_table_strategy: AttainmentTableStrategyContextI,
                 forecast_months_service: ForecastMonthsService):
        self.forecast_months_service = forecast_months_service
        self.attainment_table_strategy = attainment_table_strategy

    def evaluate_model(self, filtered_data, all_products, fe_product_growth):
        # filtered data

        closed_won_filtered_data = ExtractClosedWonDataService.extract_closed_won_data(filtered_data)
        listed_months_for_each_year = ListMonthsForEachYearServiceImpl.list_months_for_each_year(filtered_data)
        listed_products_for_each_month_for_each_year = MergeDataServiceImpl.merge_products_with_each_month_for_each_year(listed_months_for_each_year, all_products)
        monthly_totals_for_products = GetMonthlyRevenueForProductsService.get_monthly_revenue_for_products(closed_won_filtered_data)
        merged_monthly_totals_with_listed_products = MergeDataServiceImpl.merge_monthly_totals_with_listed_products(listed_products_for_each_month_for_each_year, monthly_totals_for_products)
        merged_monthly_totals_with_listed_products_with_quarters = CreateNewColumnInDataFrameServiceImpl.create_quarter_column_in_dataset(merged_monthly_totals_with_listed_products)
        calculated_quarter_totals = CalculateQuarterTotalsServiceImpl.calculate_quarter_totals(merged_monthly_totals_with_listed_products_with_quarters)

        merged_quarter_totals_with_listed_products_with_quarters = MergeDataServiceImpl.merge_quarter_totals_with_main_data_frame(merged_monthly_totals_with_listed_products_with_quarters,
                                                                                                                                  calculated_quarter_totals)

        attainment_quarter_totals_with_listed_products_with_quarters = self.attainment_table_strategy.execute_strategy(merged_quarter_totals_with_listed_products_with_quarters,
                                                                                                                       AttainmentTableType.QUARTER_TOTALS)

        calculated_yearly_totals_for_each_product = CalculateYearlyTotalsForEachProductServiceImpl.calculate_yearly_totals_for_each_product(
            merged_quarter_totals_with_listed_products_with_quarters)

        attainment_quarter_totals_merged_with_overall_data = MergeDataServiceImpl.merge_yearly_totals_with_attainment_of_quarter_totals(
            attainment_quarter_totals_with_listed_products_with_quarters,
            calculated_yearly_totals_for_each_product)

        attainment_yearly_totals_with_listed_products_with_quarters = self.attainment_table_strategy.execute_strategy(attainment_quarter_totals_merged_with_overall_data,
                                                                                                                      AttainmentTableType.YEARLY_TOTALS)

        median_calculation = CalculateMedianServiceImpl.calculate_median(attainment_yearly_totals_with_listed_products_with_quarters)

        last_year_totals_for_each_product = CalculateYearlyTotalsForEachProductServiceImpl.calculate_last_year_total_for_each_product(calculated_yearly_totals_for_each_product)
        calculated_growth_value_for_products = CalculatePercentageGrowthServiceImpl.calculate_percentage_growth(last_year_totals_for_each_product, fe_product_growth)

        median_merged_with_calculated_growth = MergeDataServiceImpl.merge_median_and_calculated_growth(median_calculation, calculated_growth_value_for_products)

        calculated_attainment_table_one = self.attainment_table_strategy.execute_strategy(median_merged_with_calculated_growth, AttainmentTableType.TABLE_ONE)

        mean_calculation = CalculateMeanServiceImpl.calculate_mean(attainment_yearly_totals_with_listed_products_with_quarters)

        median_merged_with_calculated_growth_and_mean = MergeDataServiceImpl.merge_median_calculation_to_mean_calculation(calculated_attainment_table_one, mean_calculation)
        calculated_c_model = CalculateCModelServiceImpl.calculate_c_model(median_merged_with_calculated_growth_and_mean)

        forecasted_months = self.forecast_months_service.list_months_for_forecasted_year(attainment_yearly_totals_with_listed_products_with_quarters)

        c_cmodel_final_merged_data = MergeDataServiceImpl.merge_forecasted_months_with_main_dataframe(forecasted_months, calculated_c_model)

        return c_cmodel_final_merged_data
