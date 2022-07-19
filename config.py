from main.domain.services.clean_data_service_impl import CleanDataServiceImpl
from main.domain.services.contexts.attainment_table_strategy_context import AttainmentTableStrategyContext
from main.domain.services.extract_data_based_on_number_of_years_service_impl import ExtractDataBasedOnNumberOfYearsServiceImpl
from main.domain.services.extract_unique_products_service_impl import ExtractUniqueProductsServiceImpl
from main.domain.target_data_service_impl import TargetDataServiceImpl

# https://realpython.com/python-interface/
# https: // python - dependency - injector.ets - labs.org / introduction / di_in_python.html
from main.infrastructure.repositories.file_repository_impl import FileRepositoryImpl

clean_data_service = CleanDataServiceImpl()
unique_products_service = ExtractUniqueProductsServiceImpl()
filter_data_service = ExtractDataBasedOnNumberOfYearsServiceImpl()
attainment_table_strategy = AttainmentTableStrategyContext()

target_data_service = TargetDataServiceImpl(clean_data_service=clean_data_service,
                                            unique_products_service=unique_products_service,
                                            filter_data_service=filter_data_service,
                                            attainment_table_strategy=attainment_table_strategy)

file_repository = FileRepositoryImpl()
