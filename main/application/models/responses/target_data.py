import json

from main.application.models.responses.view_models.booking import Booking
from main.application.models.responses.view_models.model_data import ModelData
from main.application.models.responses.view_models.product_data import ProductData
from main.application.models.responses.view_models.time_period import TimePeriod

# df_joined_data = pd.read_pickle('test/join_data_df.pkl')


class TargetData:
    def __init__(self, data_frame):
        self.data_frame = data_frame

    def serialize(self):

        bookings = []

        quarter_needs_to_be_removed = 0
        for i, row in self.data_frame.iterrows():

            if i % 3 == 0:
                quarter_needs_to_be_removed = quarter_needs_to_be_removed + 1

            timePeriod = TimePeriod(quarter=quarter_needs_to_be_removed, month=row['month'], month_name=row['monthName'], year=row['year']).__dict__
            productData = ProductData(group_id=i, group_name=row['Group Name'], total_revenue=row['c-model']).__dict__
            modelData = ModelData().__dict__
            booking = Booking(time_period=timePeriod, product_data=productData, model_data=modelData).__dict__
            bookings.append(booking)

        serialized = json.dumps(bookings)

        return serialized
