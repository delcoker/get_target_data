from main.domain.services.contexts.attainment_table_strategy_context_i import AttainmentTableStrategyContextI
from main.domain.services.contexts.modelling_technique_context_i import ModellingTechniqueContextI
from main.domain.services.enums.model_type import ModelType
from main.domain.services.interfaces.extract_data_service import FilterDataService
from main.domain.services.interfaces.forecast_months_service import ForecastMonthsService
from main.domain.services.strategies.modelling_techniques.c_model_service_impl import CModelServiceImpl
from main.domain.services.strategies.modelling_techniques.exponential_model_service_impl import ExponentialModelServiceImpl
from main.domain.services.strategies.modelling_techniques.linear_model_service_impl import LinearModelServiceImpl


class ModellingTechniqueContext(ModellingTechniqueContextI):

    def __init__(self, attainment_table_strategy: AttainmentTableStrategyContextI,
                 forecast_months_service: ForecastMonthsService,
                 filter_closed_won_service: FilterDataService):

        self.predefined_strategies = {ModelType.CMODEL: CModelServiceImpl(attainment_table_strategy=attainment_table_strategy,
                                                                          forecast_months_service=forecast_months_service,
                                                                          filter_closed_won_service=filter_closed_won_service),
                                      ModelType.LINEAR: LinearModelServiceImpl(forecast_months_service=forecast_months_service,
                                                                               filter_closed_won_service=filter_closed_won_service),
                                      ModelType.EXPONENTIAL: ExponentialModelServiceImpl(forecast_months_service=forecast_months_service)}

    def execute_strategy(self, strategy_type: ModelType, filtered_data, all_products, fe_product_growth):
        if strategy_type is None:
            return self.predefined_strategies[ModelType.CMODEL].evaluate_model(filtered_data, all_products, fe_product_growth)
        return self.predefined_strategies[strategy_type].evaluate_model(filtered_data, all_products, fe_product_growth)
