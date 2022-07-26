import json

from main.application.models.responses.view_models.booking import Booking
from main.application.models.responses.view_models.model_data import ModelData
from main.application.models.responses.view_models.product_data import ProductData
from main.application.models.responses.view_models.time_period import TimePeriod
from main.infrastructure.mappers.target_data_mapper import TargetDataMapper


class TargetDataMapperImpl(TargetDataMapper):

    def __init__(self):
        pass

    def serialize(self, target_data_frame) -> str:

        bookings = []

        for i, row in target_data_frame.iterrows():

            time_period = TimePeriod(quarter=row['Quarter'], month=row['Month'], month_name=row['Month_Name'], year=row['Year']).__dict__
            total_revenue = row['c_model']
            if total_revenue is None:
                total_revenue = row['ARR']
            product_data = ProductData(group_id=i, group_name=row['Product Name'], total_revenue=total_revenue).__dict__
            model_data = ModelData(median=row['Median'], growth_percent=row['Growth_Percent'], growth_value=['Growth_Value'], median_growth=['Median_Grwoth'], mean_arr=['Mean_ARR']).__dict__
            booking = Booking(time_period=time_period, product_data=product_data, model_data=model_data).__dict__
            bookings.append(booking)

        serialized = json.dumps(bookings)

        return serialized
