from models import Event
from timeline.shared_sources import NAVARRO_CIRCULATES_MEMOS_WARNING_OF_HUGE_DEATH_POTENTIAL

Event(
  date="2020-02-24",
  title="Trump says coronavirus 'very much under control', stock market is 'starting to look very good to me.'",
  description="""
  A day after Navarro warned 1-2 million people in the US could die, Trump tweeted his regular dose of nonsense.
  """,
  people=["Trump"],
  sources=[
    NAVARRO_CIRCULATES_MEMOS_WARNING_OF_HUGE_DEATH_POTENTIAL,
  ],
)
