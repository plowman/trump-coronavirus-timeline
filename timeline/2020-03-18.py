from models import Event
from timeline.shared_sources import ECDC_CASES_AND_DEATHS_BY_COUNTRY

Event(
  date="2020-03-18",
  title="US passes 100 deaths",
  description="""
  US has 108 deaths and 6,427 cases in total.
  """,
  sources=[ECDC_CASES_AND_DEATHS_BY_COUNTRY],
)
