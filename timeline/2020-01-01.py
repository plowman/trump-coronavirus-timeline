from models import Event
from timeline.shared_sources import US_INTELLIGENCE_WARNED_ABOUT_PANDEMIC

Event(
  date="2020-01-01",  # "Early January"
  title="US intelligence agencies begin warning about coronavirus",
  description="""
  U.S. intelligence agencies were issuing ominous, classified warnings in January and February about the global danger 
  posed by the coronavirus while President Trump and lawmakers played down the threat and failed to take action that 
  might have slowed the spread of the pathogen, according to U.S. officials familiar with spy agency reporting.
  """,
  people=["Trump"],
  sources=[
    US_INTELLIGENCE_WARNED_ABOUT_PANDEMIC,
  ],
)
