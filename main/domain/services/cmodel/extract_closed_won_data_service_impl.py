from main.domain.services.interfaces.extract_data_service import FilterDataService


class FilterClosedWonDataService(FilterDataService):

    def extract_closed_won_data(self):
        copy_of_dataset = self.copy()
        copy_of_dataset = self[copy_of_dataset['Stage'] == 'Closed Won']
        closed_won_data = copy_of_dataset[['Close Date', 'ARR', 'Product Name']]
        closed_won_data['Month'] = closed_won_data['Close Date'].dt.month
        closed_won_data['Year'] = closed_won_data['Close Date'].dt.strftime('%Y')
        return closed_won_data
