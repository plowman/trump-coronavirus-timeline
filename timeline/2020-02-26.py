from models import Event
from timeline.shared_sources import TRUMP_CORONAVIRUS_TIMELINE_INCREASINGLY_DAMNING

Event(
  date="2020-02-26",
  title="Trump predicts we'll covid cases within a couple days are 'going to be down to close to zero'",
  description="""
  Trump says, "When you have 15 people — and the 15 within a couple of days is going to be down to close to zero — 
  that’s a pretty good job we’ve done."
  """,
  people=["Trump"],
  sources=[
    TRUMP_CORONAVIRUS_TIMELINE_INCREASINGLY_DAMNING,
  ],
)
