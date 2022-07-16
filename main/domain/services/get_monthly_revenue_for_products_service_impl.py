from .interfaces.product_monthly_revenue_service import ProductMonthlyRevenueService

class GetMonthlyRevenueForProductsService(ProductMonthlyRevenueService):
    def get_monthly_revenue_for_products(dataset):
        dataset_copy = dataset.copy()
        product_monthly_totals = dataset_copy.groupby(['Month','Year', 'Product Name'])['ARR'].sum().reset_index()
        return product_monthly_totals
        
