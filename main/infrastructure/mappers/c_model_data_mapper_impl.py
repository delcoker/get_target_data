import math
from typing import Any, Dict

from main.application.models.responses.view_models.booking import Booking
from main.application.models.responses.view_models.c_model_data import CModelData
from main.application.models.responses.view_models.model_data import ModelData
from main.application.models.responses.view_models.product_data import ProductData
from main.application.models.responses.view_models.time_period import TimePeriod
from main.infrastructure.mappers.c_model_data_mapper import CModelDataMapper


class CModelDataMapperImpl(CModelDataMapper):

    def __init__(self):
        pass

    def serialize(self, c_model_data_frame) -> Dict[str, Any]:
        bookings = []

        for i, row in c_model_data_frame.iterrows():

            time_period = TimePeriod(quarter=row['Quarter'], month=row['Month'], month_name=row['Month_Name'], year=row['Year']).__dict__
            total_revenue = row['c_model']
            if total_revenue is None or total_revenue == '' or math.isnan(total_revenue):
                total_revenue = row['ARR']
            product_data = ProductData(group_id=row['Product Name'], group_name=row['Product Name'], total_revenue=total_revenue).__dict__
            model_data = ModelData(median=row['Median'],
                                   growth_percent=row['Growth_Percent'],
                                   growth_value=row['Growth_Value'],
                                   median_growth=row['Median_Growth'],
                                   mean_arr=row['Mean_ARR']).__dict__ if not math.isnan(row['c_model']) else ModelData().__dict__
            booking = Booking(time_period=time_period, product_data=product_data, model_data=model_data).__dict__
            bookings.append(booking)

        return CModelData(bookings).__dict__
