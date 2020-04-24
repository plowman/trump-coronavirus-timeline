from models import Event
from timeline.shared_sources import TRUMP_CORONAVIRUS_TIMELINE_INCREASINGLY_DAMNING, \
  WASHINGTON_POST_WHAT_TRUMP_DID_IN_FEBRUARY

Event(
  date="2020-02-19",
  title="Trump says, 'I think it’s going to work out fine'",
  description="""
  The full quote is “I think it’s going to work out fine. I think when we get into April, in the warmer weather, that 
  has a very negative effect on that and that type of a virus. So let’s see what happens, but I think it’s going to work
  out fine.”
  """,
  people=["Trump"],
  sources=[
    TRUMP_CORONAVIRUS_TIMELINE_INCREASINGLY_DAMNING,
  ],
)

Event(
  date="2020-02-19",
  title="Trump holds a campaign rally in Phoenix",
  description="""
  He does not mention the virus.
  """,
  people=["Trump"],
  sources=[
    WASHINGTON_POST_WHAT_TRUMP_DID_IN_FEBRUARY,
  ],
)
