from models import Event
from timeline.shared_sources import WASHINGTON_POST_WHAT_TRUMP_DID_IN_FEBRUARY

Event(
  date="2020-02-20",
  title="Trump holds campaign rally in Colorado",
  description="""
  He does not mention the virus.
  """,
  people=["Trump"],
  sources=[
    WASHINGTON_POST_WHAT_TRUMP_DID_IN_FEBRUARY,
  ],
)
