from models import Event
from timeline.shared_sources import ECDC_CASES_AND_DEATHS_BY_COUNTRY

Event(
  date="2020-03-05",
  title="US passes 10 deaths",
  description="""
  US has 11 deaths and 159 cases in total.
  """,
  sources=[ECDC_CASES_AND_DEATHS_BY_COUNTRY],
)
