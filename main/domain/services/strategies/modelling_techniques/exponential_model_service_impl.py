from main.domain.services.interfaces.forecast_months_service import ForecastMonthsService
from main.domain.services.interfaces.modelling_technique_strategy_service import ModellingTechniqueStrategyService


class ExponentialModelServiceImpl(ModellingTechniqueStrategyService):

    def __init__(self, forecast_months_service: ForecastMonthsService):
        self.forecast_months_service = forecast_months_service

    def evaluate_model(self, filtered_data, all_products, fe_product_growth):
        # filtered data

        return {"exponential": "exponential"}
