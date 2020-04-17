from models import Event
from timeline.shared_sources import ECDC_CASES_AND_DEATHS_BY_COUNTRY

Event(
  date="2020-04-12",
  title="Easter Sunday: US passes 20,000 deaths",
  description="""
  US has 20,608 deaths and 529,951 cases in total.
  
  The economy, despite Trump's encouragement on March 24th, was not "raring to go" on this day.
  """,
  sources=[ECDC_CASES_AND_DEATHS_BY_COUNTRY],
)
