from main.application.models.responses.view_models.booking import Booking


class CModelData:

    def __init__(self, bookings: [Booking]):
        self.bookings = bookings
