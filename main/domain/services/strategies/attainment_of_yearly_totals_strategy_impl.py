from main.domain.services.interfaces.attainment_table_strategy_service import AttainmentTableStrategyService


class AttainmentOfYearlyTotalsStrategyImpl(AttainmentTableStrategyService):

    def calculation(self, dataset):
        calculated_yearly_totals_for_each_product = dataset.copy()
        calculated_yearly_totals_for_each_product = calculated_yearly_totals_for_each_product.groupby(['Year', 'Product Name'])['ARR'].sum().reset_index(name='Total Arr Yearly')
        return calculated_yearly_totals_for_each_product
