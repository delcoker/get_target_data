from .interfaces.calculate_yearly_totals_for_each_product_service import CalculateYearlyTotalsForEachProductService


class CalculateYearlyTotalsForEachProductServiceImpl(CalculateYearlyTotalsForEachProductService):
    def calculate_yearly_totals_for_each_product(dataset):
        calculated_yearly_totals_for_each_product = dataset.copy()
        calculated_yearly_totals_for_each_product = calculated_yearly_totals_for_each_product.groupby(['Year', 'Product Name'])['ARR'].sum().reset_index(name='Total Arr Yearly')
        return calculated_yearly_totals_for_each_product

    def calculate_last_year_total_for_each_product(yearly_totals_for_each_product):
        last_year = yearly_totals_for_each_product.iloc[-1]['Year']
        last_year_totals_for_each_product = yearly_totals_for_each_product[['Year', 'Total Arr Yearly', 'Product Name']][yearly_totals_for_each_product['Year'] == last_year]
        return last_year_totals_for_each_product
