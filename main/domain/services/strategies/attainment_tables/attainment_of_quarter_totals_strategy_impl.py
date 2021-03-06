from main.domain.services.interfaces.attainment_table_strategy_service import AttainmentTableStrategyService


class AttainmentOfQuarterTotalsStrategyImpl(AttainmentTableStrategyService):

    def calculation(self, dataset):
        copy_of_dataset = dataset.copy()
        copy_of_dataset['ATT Quarter Total'] = copy_of_dataset['ARR'] / copy_of_dataset['Quarter Total']
        return copy_of_dataset
