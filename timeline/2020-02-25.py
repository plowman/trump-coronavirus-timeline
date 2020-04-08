from models import Event, Source
from timeline.shared_sources import US_INTELLIGENCE_WARNED_ABOUT_PANDEMIC

Event(
  date="2020-02-25",
  title="CDC official warns public about coronavirus and Trump complained it was scaring the stock market",
  description="""
  On Feb. 25, Nancy Messonnier, a senior CDC official, sounded perhaps the most significant public alarm to that point, 
  when she told reporters that the coronavirus was likely to spread within communities in the United States and that 
  disruptions to daily life could be “severe.” Trump called Azar on his way back from a trip to India and complained 
  that Messonnier was scaring the stock markets, according to two senior administration officials.
  """,
  people=["Trump", "Azar", "Nancy Messonier"],
  sources=[
    US_INTELLIGENCE_WARNED_ABOUT_PANDEMIC,
  ],
)

Event(
  date="2020-02-25",
  title="Dr. Helen Chu defies government order to test for the coronavirus and discovers it's already in the US",
  description="""
  Dr. Chu and her colleagues had been gathering nasal swabs from people in the Seattle area experiencing flu symptoms.
  She sought permission from the government and was rejected multiple times.
  
  Finally, they started testing anyway and soon discovered a teen with no recent travel history who had coronavirus.
  
  If the federal government had granted her earlier permission, we could have known much sooner about community spread
  in the US.
  """,
  people=["Helen Chu"],
  sources=[
    Source(
      title="‘It’s Just Everywhere Already’: How Delays in Testing Set Back the U.S. Coronavirus Response",
      publication="The New York Times",
      published="2020-03-10",
      url="https://www.nytimes.com/2020/03/10/us/coronavirus-testing-delays.html",
      article_copy="./sources/2020-03-10-its-just-everywhere-already.pdf",
    ),
  ],
)
