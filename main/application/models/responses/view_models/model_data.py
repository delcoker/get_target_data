from main.application.models.responses.view_models.enums.model_type import ModelType
from main.application.models.responses.view_models.enums.revenue_type import RevenueType


class ModelData:
    def __init__(self, median=0, mean=0, forecast=0, total_revenue=0, revenue_type=RevenueType.RECURRING_REVENUE, model_type=ModelType.CMODEL):
        self.median = median
        self.mean = mean
        self.forecast = forecast
        self.totalRevenue = total_revenue
        self.revenueType = revenue_type
        self.modelType = model_type
