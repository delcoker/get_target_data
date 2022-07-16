from main.domain.services.calculate_attainment_of_quarter_totals_service_impl import CalculateAttainmentOfQuarterTotalsServiceImpl
from main.domain.services.calculate_attainment_of_yearly_totals_service_impl import CalculateAttainmentOfYearlyTotalsServiceImpl
from main.domain.services.calculate_attainment_table_one_service_impl import CalculateAttainmentTableOneServiceImpl
from main.domain.services.calculate_c_model_service_impl import CalculateCModelServiceImpl
from main.domain.services.calculate_mean_service_impl import CalculateMeanServiceImpl
from main.domain.services.calculate_median_service_impl import CalculateMedianServiceImpl
from main.domain.services.calculate_percentage_growth_service_impl import CalculatePercentageGrowthServiceImpl
from main.domain.services.calculate_quarter_totals_service_impl import CalculateQuarterTotalsServiceImpl
from main.domain.services.calculate_yearly_totals_for_each_product_service_impl import CalculateYearlyTotalsForEachProductServiceImpl
from main.domain.services.create_new_column_in_data_frame_service_impl import CreateNewColumnInDataFrameServiceImpl
from main.domain.services.extract_closed_won_data_service_impl import ExtractClosedWonDataService
from main.domain.services.extract_data_based_on_number_of_years_service_impl import ExtractDataBasedOnNumberOfYearsServiceImpl
from main.domain.services.get_monthly_revenue_for_products_service_impl import GetMonthlyRevenueForProductsService
from main.domain.services.interfaces.data_etl_service import DataEtlService
from main.domain.services.interfaces.extract_unique_products_service import UniqueProductsService
from main.domain.services.list_months_for_each_year_service_impl import ListMonthsForEachYearServiceImpl
from main.domain.services.merge_data_service_impl import MergeDataServiceImpl
from main.domain.target_data_service import TargetDataService


# https://python-dependency-injector.ets-labs.org/introduction/di_in_python.html
class TargetDataServiceImpl(TargetDataService):
    def __init__(self, clean_data_service: DataEtlService,
                 unique_products_service: UniqueProductsService):
        self.clean_data_service = clean_data_service
        self.unique_products_service = unique_products_service

    def get_target_data(self, fe_product_growth, dirty_data):
        cleaned_data = self.clean_data_service.standard_data_clean(dirty_data)
        all_products = self.unique_products_service.get_unique_products(cleaned_data)

        filtered_data = ExtractDataBasedOnNumberOfYearsServiceImpl.extract_data_based_on_number_of_years(cleaned_data)
        closed_won_filtered_data = ExtractClosedWonDataService.extract_closed_won_data(filtered_data)
        listed_months_for_each_year = ListMonthsForEachYearServiceImpl.list_months_for_each_year(filtered_data)
        listed_products_for_each_month_for_each_year = MergeDataServiceImpl.merge_products_with_each_month_for_each_year(listed_months_for_each_year, all_products)
        monthly_totals_for_products = GetMonthlyRevenueForProductsService.get_monthly_revenue_for_products(closed_won_filtered_data)
        merged_monthly_totals_with_listed_products = MergeDataServiceImpl.merge_monthly_totals_with_listed_products(listed_products_for_each_month_for_each_year, monthly_totals_for_products)
        merged_monthly_totals_with_listed_products_with_quarters = CreateNewColumnInDataFrameServiceImpl.create_quarter_column_in_dataset(merged_monthly_totals_with_listed_products)
        calculated_quarter_totals = CalculateQuarterTotalsServiceImpl.calculate_quarter_totals(merged_monthly_totals_with_listed_products_with_quarters)

        merged_quarter_totals_with_listed_products_with_quarters = MergeDataServiceImpl.merge_quarter_totals_with_main_data_frame(merged_monthly_totals_with_listed_products_with_quarters,
                                                                                                                                  calculated_quarter_totals)
        attainment_quarter_totals_with_listed_products_with_quarters = CalculateAttainmentOfQuarterTotalsServiceImpl.calculate_attainment_of_quarter_totals(
            merged_quarter_totals_with_listed_products_with_quarters)
        calculated_yearly_totals_for_each_product = CalculateYearlyTotalsForEachProductServiceImpl.calculate_yearly_totals_for_each_product(
            merged_quarter_totals_with_listed_products_with_quarters)
        attainment_quarter_totals_merged_with_overall_data = MergeDataServiceImpl.merge_yearly_totals_with_attainment_of_quarter_totals(
            attainment_quarter_totals_with_listed_products_with_quarters,
            calculated_yearly_totals_for_each_product)

        attainment_yearly_totals_with_listed_products_with_quarters = CalculateAttainmentOfYearlyTotalsServiceImpl.calculate_attainment_of_yearly_totals(
            attainment_quarter_totals_merged_with_overall_data)
        median_calculation = CalculateMedianServiceImpl.calculate_median(attainment_yearly_totals_with_listed_products_with_quarters)

        last_year_totals_for_each_product = CalculateYearlyTotalsForEachProductServiceImpl.calculate_last_year_total_for_each_product(calculated_yearly_totals_for_each_product)
        calculated_growth_value_for_products = CalculatePercentageGrowthServiceImpl.calculate_percentage_growth(last_year_totals_for_each_product, fe_product_growth)

        median_merged_with_calculated_growth = MergeDataServiceImpl.merge_median_and_calculated_growth(median_calculation, calculated_growth_value_for_products)
        calculated_attainment_table_one = CalculateAttainmentTableOneServiceImpl.calculate_attainment_attainment_table(median_merged_with_calculated_growth)

        mean_calculation = CalculateMeanServiceImpl.calculate_mean(attainment_yearly_totals_with_listed_products_with_quarters)

        median_merged_with_calculated_growth_and_mean = MergeDataServiceImpl.merge_median_calculation_to_mean_calculation(calculated_attainment_table_one, mean_calculation)
        calculated_c_model = CalculateCModelServiceImpl.calculate_c_model(median_merged_with_calculated_growth_and_mean)

        return calculated_c_model

        pass
