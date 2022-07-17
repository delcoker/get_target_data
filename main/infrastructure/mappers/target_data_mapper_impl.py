import json

from main.application.models.responses.view_models.booking import Booking
from main.application.models.responses.view_models.model_data import ModelData
from main.application.models.responses.view_models.product_data import ProductData
from main.application.models.responses.view_models.time_period import TimePeriod
from main.infrastructure.mappers.target_data_mapper import TargetDataMapper


class TargetDataMapperImpl(TargetDataMapper):
    def __init__(self):
        pass

    def serialize(self, data_frame) -> str:

        bookings = []

        quarter_needs_to_be_removed = 0
        for i, row in data_frame.iterrows():

            if i % 3 == 0:
                quarter_needs_to_be_removed = quarter_needs_to_be_removed + 1

            time_period = TimePeriod(quarter=quarter_needs_to_be_removed, month=row['month'], month_name=row['monthName'], year=row['year']).__dict__
            product_data = ProductData(group_id=i, group_name=row['Group Name'], total_revenue=row['c-model']).__dict__
            model_data = ModelData().__dict__
            booking = Booking(time_period=time_period, product_data=product_data, model_data=model_data).__dict__
            bookings.append(booking)

        serialized = json.dumps(bookings)

        return serialized
