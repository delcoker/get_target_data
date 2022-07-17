class Booking:
    def __init__(self, time_period=None, product_data=None, model_data=None):
        self.modelData = model_data
        self.productData = product_data
        self.timePeriod = time_period

    def __str__(self):
        return self.__dict__

    def __repr__(self):
        return self.__dict__
