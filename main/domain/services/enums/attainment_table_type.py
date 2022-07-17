from enum import Enum


# https://py.watch/convert-a-python-enum-to-json-5eb5e94ecc9
class AttainmentTableType(str, Enum):
    QUARTER_TOTALS = 'quarter totals'
    YEARLY_TOTALS = 'yearly totals'
    TABLE_ONE = "table one"
