class ProductData:
    def __init__(self, group_id, group_name, total_revenue):
        self.groupId = group_id
        self.groupName = group_name
        self.totalRevenue = total_revenue

    def __str__(self):
        return self.__dict__

    def __repr__(self):
        return self.__dict__
