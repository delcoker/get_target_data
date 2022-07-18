from main.domain.services.contexts.attainment_table_strategy_context_i import AttainmentTableStrategyContextI
from main.domain.services.enums.attainment_table_type import AttainmentTableType
from main.domain.services.strategies.attainment_tables.attainment_of_quarter_totals_strategy_impl import AttainmentOfQuarterTotalsStrategyImpl
from main.domain.services.strategies.attainment_tables.attainment_of_table_one_strategy_impl import AttainmentTableOneStrategyImpl
from main.domain.services.strategies.attainment_tables.attainment_of_yearly_totals_strategy_impl import AttainmentOfYearlyTotalsStrategyImpl


class AttainmentTableStrategyContext(AttainmentTableStrategyContextI):

    def __init__(self):
        self.predefined_strategies = {AttainmentTableType.QUARTER_TOTALS: AttainmentOfQuarterTotalsStrategyImpl(),
                                      AttainmentTableType.YEARLY_TOTALS: AttainmentOfYearlyTotalsStrategyImpl(),
                                      AttainmentTableType.TABLE_ONE: AttainmentTableOneStrategyImpl()}

    def execute_strategy(self, dataset, strategy_type: AttainmentTableType):
        return self.predefined_strategies[strategy_type].calculation(dataset)
