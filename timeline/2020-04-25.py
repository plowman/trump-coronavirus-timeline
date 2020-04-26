from models import Event
from timeline.shared_sources import ECDC_CASES_AND_DEATHS_BY_COUNTRY

Event(
  date="2020-04-25",
  title="US passes 50,000 deaths",
  description="""
  US has 51,017 deaths and 890,524 cases in total.
  """,
  sources=[ECDC_CASES_AND_DEATHS_BY_COUNTRY],
)
