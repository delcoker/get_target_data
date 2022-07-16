import pandas as pd
from .interfaces.extract_unique_products_service import UniqueProductsService


class ExtractUniqueProductsServiceImpl(UniqueProductsService):
    def __init__(self):
        pass

    def get_unique_products(self, dataset):
        all_products = (pd.unique(dataset['Product Name']))
        return all_products
