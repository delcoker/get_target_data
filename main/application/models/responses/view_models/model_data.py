from main.domain.services.enums.model_type import ModelType
from main.application.models.responses.view_models.enums.revenue_type import RevenueType


class ModelData:
    def __init__(self, median=0, growth_percent=0, growth_value=0, median_growth=0, mean_arr=0, revenue_type=RevenueType.RECURRING_REVENUE, model_type=ModelType.CMODEL):
        self.median = median
        self.growth_percent = growth_percent
        self.growth_value = growth_value
        self.median_growth = median_growth
        self.mean_arr = mean_arr
        self.revenueType = revenue_type
        self.modelType = model_type

    def __str__(self):
        return self.__dict__

    def __repr__(self):
        return self.__dict__
