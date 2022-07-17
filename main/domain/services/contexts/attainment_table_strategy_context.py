from main.domain.services.interfaces.attainment_table_strategy_service import AttainmentTableStrategyService


class AttainmentTableStrategyContext:
    def __init__(self, strategy_type: AttainmentTableStrategyService):
        self.strategy = strategy_type

    def execute_strategy(self, dataset):
        return self.strategy.calculation(dataset)
