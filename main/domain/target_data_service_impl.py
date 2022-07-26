import urllib3
from pandas import DataFrame

from main.domain.services.contexts.modelling_technique_context_i import ModellingTechniqueContextI
from main.domain.services.enums.model_type import ModelType
from main.domain.services.interfaces.data_etl_service import DataEtlService
from main.domain.services.interfaces.extract_data_service import FilterDataService
from main.domain.services.interfaces.extract_unique_products_service import UniqueProductsService
from main.domain.target_data_service import TargetDataService


class TargetDataServiceImpl(TargetDataService):
    def __init__(self, clean_data_service: DataEtlService,
                 unique_products_service: UniqueProductsService,
                 filter_data_service: FilterDataService,
                 modelling_technique_strategy: ModellingTechniqueContextI):
        self.clean_data_service = clean_data_service
        self.unique_products_service = unique_products_service
        self.filtered_data_service = filter_data_service
        self.modelling_technique_strategy = modelling_technique_strategy

    def get_target_data(self, fe_product_growth, dirty_data) -> DataFrame:
        cleaned_data = self.clean_data_service.standard_data_clean(dirty_data)
        all_products = self.unique_products_service.get_unique_products(cleaned_data)
        filtered_data = self.filtered_data_service.extract_data_based_on_number_of_years(cleaned_data)
        # print(filtered_data)
        c_cmodel_data_frame = self.modelling_technique_strategy.execute_strategy(ModelType.CMODEL, filtered_data, all_products, fe_product_growth)
        linear_model_data_frame = self.modelling_technique_strategy.execute_strategy(ModelType.LINEAR, filtered_data, all_products, fe_product_growth)
        exponential_model_data_frame = self.modelling_technique_strategy.execute_strategy(ModelType.EXPONENTIAL, filtered_data, all_products, fe_product_growth)

        # sagemaker_model = self.get_sagemaker_model()  # worked like a charm

        return c_cmodel_data_frame

    def get_sagemaker_model(self):
        api = "https://z0gyxki6ob.execute-api.us-east-1.amazonaws.com/prod/dummy"
        http = urllib3.PoolManager()
        response = http.request('GET', api)
        # sage_maker_status = json.load(response.data.decode('utf-8'))
        sage_maker_status = response.data
        # print(sage_maker_status)
        return sage_maker_status
