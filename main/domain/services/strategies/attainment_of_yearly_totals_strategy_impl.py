from main.domain.services.interfaces.attainment_table_strategy_service import AttainmentTableStrategyService


class AttainmentOfYearlyTotalsStrategyImpl(AttainmentTableStrategyService):

    def calculation(self, dataset):
        copy_of_dataset = dataset.copy()
        copy_of_dataset['ATT Year Total'] = copy_of_dataset['ARR'] / copy_of_dataset['Total Arr Yearly']
        return copy_of_dataset
