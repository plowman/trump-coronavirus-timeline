from models import Event
from timeline.shared_sources import NAVARRO_CIRCULATES_MEMOS_WARNING_OF_HUGE_DEATH_POTENTIAL

Event(
  date="2020-01-29",
  title="Trump is notified of Navarro memo warning 543,000 Americans could die",
  description="""
  Trump economic advisor Peter Navarro circulated in the White House warning that there would be a dire human and 
  economic costs. He specifically warns that an outbreak in the US could cost the economy up to $5.7 Trillion and as 
  many as 543,000 people could die.

  It is unclear whether the president ever read this memo, though he was notified of it.
  """,
  people=["Navarro", "Trump"],
  sources=[
    NAVARRO_CIRCULATES_MEMOS_WARNING_OF_HUGE_DEATH_POTENTIAL,
  ],
)
