from main.domain.services.clean_data_service_impl import CleanDataServiceImpl
from main.domain.services.cmodel.extract_closed_won_data_service_impl import FilterClosedWonDataServiceImpl
from main.domain.services.contexts.attainment_table_strategy_context import AttainmentTableStrategyContext
from main.domain.services.contexts.modelling_technique_context import ModellingTechniqueContext
from main.domain.services.cmodel.filter_data_by_year_service_impl import FilterDataByYearServiceImpl
from main.domain.services.extract_unique_products_service_impl import ExtractUniqueProductsServiceImpl
from main.domain.services.strategies.modelling_techniques.c_model_service_impl import CModelServiceImpl
from main.domain.target_data_service_impl import TargetDataServiceImpl
from main.domain.services.forecast_months_service_impl import ForecastMonthsServiceImpl
from main.infrastructure.repositories.file_repository_impl import FileRepositoryImpl

clean_data_service = CleanDataServiceImpl()
unique_products_service = ExtractUniqueProductsServiceImpl()
filter_data_service = FilterDataByYearServiceImpl()
attainment_table_strategy = AttainmentTableStrategyContext()
forecast_months_service = ForecastMonthsServiceImpl()
filter_closed_won_service = FilterClosedWonDataServiceImpl()

c_model_service = CModelServiceImpl(attainment_table_strategy=attainment_table_strategy,
                                    forecast_months_service=forecast_months_service,
                                    filter_closed_won_service=filter_closed_won_service)

modelling_technique_strategy = ModellingTechniqueContext(attainment_table_strategy=attainment_table_strategy,
                                                         forecast_months_service=forecast_months_service,
                                                         filter_closed_won_service=filter_closed_won_service)

target_data_service = TargetDataServiceImpl(clean_data_service=clean_data_service,
                                            unique_products_service=unique_products_service,
                                            filter_data_service=filter_data_service,
                                            modelling_technique_strategy=modelling_technique_strategy)

file_repository = FileRepositoryImpl()
