from main.domain.services.interfaces.extract_data_service import FilterDataService


class FilterClosedWonDataServiceImpl(FilterDataService):
    def __init__(self):
        pass

    def extract_closed_won_data(self, dataset):
        copy_of_dataset = dataset.copy()
        copy_of_dataset = dataset[copy_of_dataset['Stage'] == 'Closed Won']
        closed_won_data = copy_of_dataset[['Close Date', 'ARR', 'Product Name']]
        closed_won_data['Month'] = closed_won_data['Close Date'].dt.month
        closed_won_data['Year'] = closed_won_data['Close Date'].dt.strftime('%Y')
        return closed_won_data
