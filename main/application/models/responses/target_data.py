from main.application.models.responses.view_models.c_model_data import CModelData


class TargetData:

    def __init__(self, c_model_data: CModelData, linear_data=None, exponential_data=None):
        self.cModelData = c_model_data
        self.linearData = linear_data
        self.exponentialData = exponential_data
