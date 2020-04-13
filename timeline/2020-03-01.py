from models import Event
from timeline.shared_sources import ECDC_CASES_AND_DEATHS_BY_COUNTRY

Event(
  date="2020-03-01",
  title="US has first death",
  description="""
  US has 1 death and 69 cases.
  """,
  sources=[ECDC_CASES_AND_DEATHS_BY_COUNTRY],
)




# 2020-03-01 - 1 death
# 2020-03-05 - passes 10 deaths, (11 deaths, 159 cases)
# 2020-03-18 - passes 100 deaths, (108 deaths, 6,427 cases)
# 2020-03-26 - passes 1,000 deaths, (1,050 deaths, 69,194 cases)
# 2020-04-07 - passes 10,000 deaths, (10,989 deaths, 368,196 cases)
