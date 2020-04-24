from models import Event
from timeline.shared_sources import WASHINGTON_POST_WHAT_TRUMP_DID_IN_FEBRUARY

Event(
  date="2020-02-01",
  title="Trump plays golf at Mar-a-Lago",
  description="""
  In his defense, since the virus was going to go away on its own, there's not much he could do anyway.
  """,
  people=["Trump"],
  sources=[
    WASHINGTON_POST_WHAT_TRUMP_DID_IN_FEBRUARY,
  ],
)
