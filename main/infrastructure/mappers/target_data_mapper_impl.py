import json

from main.application.models.responses.target_data import TargetData
from main.infrastructure.mappers.c_model_data_mapper import CModelDataMapper
from main.infrastructure.mappers.target_data_mapper import TargetDataMapper


class TargetDataMapperImpl(TargetDataMapper):

    def __init__(self, c_model_data_mapper: CModelDataMapper):
        self.c_model_data_mapper = c_model_data_mapper

    def serialize(self, target_data_frame) -> str:

        c_model_data = self.c_model_data_mapper.serialize(c_model_data_frame=target_data_frame)

        target_data = TargetData(c_model_data=c_model_data).__dict__

        serialized = json.dumps(target_data)

        return serialized
