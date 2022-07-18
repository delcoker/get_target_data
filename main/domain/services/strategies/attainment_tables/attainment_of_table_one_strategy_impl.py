from main.domain.services.interfaces.attainment_table_strategy_service import AttainmentTableStrategyService


class AttainmentTableOneStrategyImpl(AttainmentTableStrategyService):

    def calculation(self, dataset):
        copy_of_dataset = dataset.copy()
        copy_of_dataset['Median_Growth'] = copy_of_dataset['Median'] * copy_of_dataset['Growth_Value']
        copy_of_dataset['Median_Growth'] = copy_of_dataset['Median_Growth'].round(decimals=2)

        return copy_of_dataset
