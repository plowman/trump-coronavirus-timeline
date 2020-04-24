from models import Event, Source
from timeline.shared_sources import WASHINGTON_POST_WHAT_TRUMP_DID_IN_FEBRUARY

Event(
  date="2020-02-02",
  title="China travel ban begins, does not change entry for US citizens",
  description="""
  The travel ban prevents travel to the US if you've been to mainland China in the past 14 days. However, the ban does 
  not apply to US citizens and their families. As a result, 40,000 people have traveled from China to the US from when 
  the ban began until April 4th.
  
  For those 40,000 there was little to no actual preventive measures. As far as I can tell, nobody was tested for covid 
  and nobody was required to quarantine. Occasionally your temperature would be taken at an airport, and usually you 
  would be asked to stay home for 14 days.
  
  From the New York Times article:
  > Re-entry to the US during this time is very lax. A traveler from Beijing going to Seattle was asked if he had a
    temperature and whether he had been to Wuhan. They gave him a card requesting he stay home for two weeks. Nobody 
    ever followed up.
  """,
  people=["Trump"],
  sources=[
    Source(
      title="430,000 People Have Traveled From China to U.S. Since Coronavirus Surfaced",
      publication="The New York Times",
      published="2020-04-04",
      url="https://www.nytimes.com/2020/04/04/us/coronavirus-china-travel-restrictions.html",
      article_copy="sources/2020-04-04-new-york-times-coronavirus-travel-restrictions.pdf",
    ),
    Source(
      title="Proclamation on Suspension of Entry as Immigrants and Nonimmigrants of Persons who Pose a Risk of "
            "Transmitting 2019 Novel Coronavirus",
      publication="The White House",
      published="2020-01-31",
      url="https://www.whitehouse.gov/presidential-actions/proclamation-suspension-entry-immigrants-nonimmigrants-persons-pose-risk-transmitting-2019-novel-coronavirus/",
      article_copy="sources/2020-01-31-white-house-china-ban-announcement.pdf",
    ),
  ],
)

Event(
  date="2020-02-02",
  title="Trump plays golf again, says he 'shut it down coming in from China'",
  description="""
  After playing golf, he sat for a classic Hannity softball where he added, “Well, we pretty much shut it down coming in
  from China,”
  """,
  people=["Trump"],
  sources=[
    WASHINGTON_POST_WHAT_TRUMP_DID_IN_FEBRUARY,
  ],
)
