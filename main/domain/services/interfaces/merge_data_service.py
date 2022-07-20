class MergeDataService:
    def merge_products_with_each_month_for_each_year(self, full_file_name: str, all_products) -> dict:
        """Get all months for each year from the currently loaded file."""
        pass

    def merge_monthly_totals_with_listed_products(self, listed_products_for_each_month_for_each_year, monthly_totals) -> dict:
        """Get all months for each year from the currently loaded file."""
        pass

    def merge_quarter_totals_with_main_data_frame(self, merged_monthly_totals_with_listed_products_with_quarters, quarter_totals) -> dict:
        """Get all months for each year from the currently loaded file."""
        pass

    def merge_yearly_totals_with_attainment_of_quarter_totals(self, attainment_quarter_totals, yearly_totals) -> dict:
        """Merge attainment of quarter totals with yearly totals from the currently loaded file."""
        pass

    def merge_median_and_calculated_growth(self, median_calculation, calculated_product_growth) -> dict:
        """Merge median calculation for forecasted months with calculated product growth from the currently loaded file."""
        pass

    def merge_median_calculation_to_mean_calculation(self, median_growth_calculation, mean_calculation) -> dict:
        """Merge median calculation for forecasted months with calculated product growth from the currently loaded file."""
        pass

    def merge_forecasted_months_with_main_dataframe(self, forecast_months, dataset) -> dict:
        """Merge forecasted months with main dataframe from the currently loaded files."""
        pass

    def append_previous_years_with_forecasted_data(self, previous_years, forecasted_data) -> dict:
        """Append previous years data with main dataframe from the currently loaded files."""
        pass