from .interfaces.calculate_attainment_table_one_service import CalculateAttainmentTableOneService


class CalculateAttainmentTableOneServiceImpl(CalculateAttainmentTableOneService):
    def calculate_attainment_attainment_table(dataset):
        copy_of_dataset = dataset.copy()
        copy_of_dataset['Median_Growth'] = copy_of_dataset['Median'] * copy_of_dataset['Growth_Value']
        copy_of_dataset['Median_Growth'] = copy_of_dataset['Median_Growth'].round(decimals=2)

        return copy_of_dataset
