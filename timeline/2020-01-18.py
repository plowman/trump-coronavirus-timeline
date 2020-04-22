from models import Event
from timeline.shared_sources import TRUMP_CORONAVIRUS_TIMELINE_INCREASINGLY_DAMNING

Event(
  date="2020-01-18",
  title="HHS Secretary Azar talks to Trump about coronavirus, Trump asks about the vaping ban",
  description="""
  Despite earlier efforts, this is the first time he was able to speak with Trump.
  
  From the article,
  > When he reached Trump by phone, the president interjected to ask about vaping and when flavored vaping products 
  would be back on the market, the senior administration officials said.
  """,
  people=["Azar", "Trump"],
  sources=[
    TRUMP_CORONAVIRUS_TIMELINE_INCREASINGLY_DAMNING,
  ],
)
