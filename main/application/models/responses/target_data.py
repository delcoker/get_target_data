from main.application.models.responses.view_models.c_model_data import CModelData


class TargetData:

    def __init__(self, c_model_data: CModelData, linear_model_data=None, exponential_model_data=None):
        self.cModelData = c_model_data
        self.linearModelData = linear_model_data
        self.exponentialModelData = exponential_model_data
