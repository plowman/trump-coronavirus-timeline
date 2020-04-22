from models import Event, Source
from timeline.shared_sources import TRUMP_CORONAVIRUS_TIMELINE_INCREASINGLY_DAMNING

Event(
  date="2020-01-30",
  title="Azar tells Trump of the potential for a pandemic",
  description="""
  HHS Secretary Alex Azar once again tries to warn the president that this could get really bad. The president responded
  that Azar was being alarmist.
  """,
  people=["Azar", "Trump"],
  sources=[
    Source(
      title="He Could Have Seen What Was Coming: Behind Trump’s Failure on the Virus",
      publication="The New York Times",
      published="2020-04-11",
      url="https://www.nytimes.com/2020/04/11/us/politics/coronavirus-trump-response.html",
      article_copy="sources/2020-04-11-new-york-times-he-could-have-seen.pdf",
    ),
  ],
)

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
