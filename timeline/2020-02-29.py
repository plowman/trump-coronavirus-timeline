from models import Event, Source
from timeline.shared_sources import WASHINGTON_POST_WHAT_TRUMP_DID_IN_FEBRUARY

Event(
  date="2020-02-29",
  title="WHO has shipped tests to 60 countries, and the US is not among them.",
  description="""
  Three weeks after releasing flawed CDC tests, the US has still not requested the WHO tests. The bottleneck is clearly
  not the WHO because at this point the WHO has sent tests to 60 countries.
  """,
  people=[],
  sources=[
    Source(
      title="How testing failures allowed coronavirus to sweep the U.S.",
      publication="Politico",
      published="2020-03-06",
      url="https://www.politico.com/news/2020/03/06/coronavirus-testing-failure-123166",
      article_copy="./sources/2020-03-06-politico-how-testing-failures.pdf",
    ),
  ],
)

Event(
  date="2020-02-29",
  title="Trump says if you're healthy and infected, 'you will probably go through a process and you’ll be fine.'",
  description="""
  His full quote is:
  > “Additional cases in the United States are likely, but healthy individuals should be able to fully recover. And we 
  think that will be a statement that we can make with great surety now that we’ve gotten familiar with this problem. 
  They should be able to recover should they contract the virus. So, healthy people, if you’re healthy, you will 
  probably go through a process and you’ll be fine.”
  """,
  people=["Trump"],
  sources=[
    WASHINGTON_POST_WHAT_TRUMP_DID_IN_FEBRUARY,
  ],
)
