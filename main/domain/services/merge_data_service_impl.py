from main.domain.services.interfaces.merge_data_service import MergeDataService
import pandas as pd
import calendar


class MergeDataServiceImpl(MergeDataService):
    def merge_products_with_each_month_for_each_year(dataset, all_products):
        # copy_of_dataset = dataset.copy()
        product_data_list = pd.DataFrame()
        for product in all_products:
            temp_copy = dataset.copy()
            temp_copy['Product Name'] = product
            product_data_list = pd.concat([product_data_list, temp_copy])

        product_data_list = product_data_list.sort_values(['Product Name', 'Year', 'Month']).reset_index(drop=True)

        return product_data_list

    def merge_monthly_totals_with_listed_products(listed_products_for_each_month_for_each_year, monthly_totals):
        listed_products_for_each_month_for_each_year['Month'] = listed_products_for_each_month_for_each_year['Month'].astype(int)
        listed_products_for_each_month_for_each_year['Year'] = listed_products_for_each_month_for_each_year['Year'].astype(int)

        monthly_totals['Month'] = monthly_totals['Month'].astype(int)
        monthly_totals['Year'] = monthly_totals['Year'].astype(int)

        merged_monthly_totals_with_listed_products = pd.merge(listed_products_for_each_month_for_each_year, monthly_totals, how="left", on=["Month", "Year", "Product Name"])
        return merged_monthly_totals_with_listed_products

    def merge_quarter_totals_with_main_data_frame(merged_monthly_totals_with_listed_products_with_quarters, quarter_totals):
        merged_quarter_totals_with_main_data_frame = pd.merge(merged_monthly_totals_with_listed_products_with_quarters, quarter_totals, how="left", on=["Quarter", "Year", "Product Name"])
        return merged_quarter_totals_with_main_data_frame

    def merge_yearly_totals_with_attainment_of_quarter_totals(dataset, yearly_totals):
        attainment_quarter_totals_merged_with_overall_data = pd.merge(dataset, yearly_totals, how="left", on=["Year", "Product Name"])
        return attainment_quarter_totals_merged_with_overall_data

    def merge_median_and_calculated_growth(median_calculation, calculated_product_growth):
        median_merged_with_calculated_growth = pd.merge(median_calculation, calculated_product_growth, on="Product Name", how="left")
        return median_merged_with_calculated_growth

    def merge_median_calculation_to_mean_calculation(median_calculation, mean_calculation):
        merged_median_and_mean = pd.merge(median_calculation, mean_calculation, how="left")
        merged_median_and_mean['Month_Name'] = merged_median_and_mean['Month'].apply(lambda x: calendar.month_abbr[x])
        return merged_median_and_mean

    def merge_forecasted_months_with_main_dataframe(forecast_months, dataset):
        merged_data = pd.merge(forecast_months[['Month', 'Year']], dataset, on='Month', how='left')
        return merged_data
