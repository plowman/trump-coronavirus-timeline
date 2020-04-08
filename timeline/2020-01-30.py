from models import Event
from timeline.shared_sources import TRUMP_CORONAVIRUS_TIMELINE_INCREASINGLY_DAMNING

Event(
  date="2020-01-30",
  title="Trump says 'We think it’s going to have a very good ending for it. So that I can assure you.'",
  description="""
  That's the whole quote. I haven't dug into the original source yet.
  """,
  people=["Trump"],
  sources=[
    TRUMP_CORONAVIRUS_TIMELINE_INCREASINGLY_DAMNING,
  ],
)
