from .interfaces.calculate_percentage_growth_service import CalculatePercentageGrowthService
import pandas as pd


class CalculatePercentageGrowthServiceImpl(CalculatePercentageGrowthService):
    def calculate_percentage_growth(last_year_totals_for_each_product, fe_product_growth):
        be_product_growth = []
        for product in fe_product_growth['data']:
            # be_product_growth[product['product']] = {}
            convert_percentage_growth_to_decimal = product['growth'] / 100
            product_row_for_yealy_arr_total = last_year_totals_for_each_product.loc[last_year_totals_for_each_product['Product Name'] == product['product']]
            get_arr_value = product_row_for_yealy_arr_total['Total Arr Yearly'].values[0]
            product_growth = convert_percentage_growth_to_decimal * get_arr_value
            new_product_obj = {"product": product['product'], "Growth_Percent": product['growth'], "Growth_Value": product_growth}
            be_product_growth.append(new_product_obj)
        be_product_growth = pd.DataFrame(be_product_growth)
        be_product_growth = be_product_growth.rename(columns={'product': 'Product Name'})
        return be_product_growth
