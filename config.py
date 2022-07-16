from main.domain.services.clean_data_service_impl import CleanDataServiceImpl
from main.domain.services.extract_unique_products_service_impl import ExtractUniqueProductsServiceImpl
from main.domain.target_data_service_impl import TargetDataServiceImpl

# https://realpython.com/python-interface/
# https: // python - dependency - injector.ets - labs.org / introduction / di_in_python.html
clean_data_service = CleanDataServiceImpl()
unique_products_service = ExtractUniqueProductsServiceImpl()


target_data_service = TargetDataServiceImpl(clean_data_service=clean_data_service, unique_products_service=unique_products_service)
