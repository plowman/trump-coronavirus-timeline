from models import Event
from timeline.shared_sources import ECDC_CASES_AND_DEATHS_BY_COUNTRY

Event(
  date="2020-03-26",
  title="US passes 1,000 deaths",
  description="""
  US has 1,050 deaths and 69,194 cases in total.
  """,
  sources=[ECDC_CASES_AND_DEATHS_BY_COUNTRY],
)
