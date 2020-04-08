from models import Event
from timeline.shared_sources import TRUMP_CORONAVIRUS_TIMELINE_INCREASINGLY_DAMNING

Event(
  date="2020-01-22",
  title="Trump's first comments on Coronavirus: 'we have it totally under control. ... It’s going to be just fine.'",
  description="""
  President Trump made his first public comments about the coronavirus in a TV interview from Davos with CNBC’s Joe 
  Kernen. The first American case had been announced the day before, and Kernen asked Trump, “Are there worries about a 
  pandemic at this point?”

  Trump said, “No. Not at all. And we have it totally under control. It’s one person coming in from China, and we have 
  it under control. It’s going to be just fine.”
  """,
  people=["Trump", "Joe Kernen"],
  sources=[
    TRUMP_CORONAVIRUS_TIMELINE_INCREASINGLY_DAMNING,
  ],
)
