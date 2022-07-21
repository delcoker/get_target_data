from main.domain.services.interfaces.calculate_c_model_service import CalculateCModelService


class CalculateCModelServiceImpl(CalculateCModelService):

    def calculate_c_model(dataset):
        c_model_calculated = dataset.copy()
        c_model_calculated['c_model'] = c_model_calculated['Median_Growth'] + c_model_calculated['Mean_ARR']
        return c_model_calculated
