from models import Event, Source
from timeline.shared_sources import ECDC_CASES_AND_DEATHS_BY_COUNTRY

Event(
  date="2020-03-18",
  title="US passes 100 deaths",
  description="""
  US has 108 deaths and 6,427 cases in total.
  """,
  sources=[ECDC_CASES_AND_DEATHS_BY_COUNTRY],
)

Event(
  date="2020-03-18",
  title="US still has not filled our WHO Executive Board seat",
  description="""
  The White House renewed its nomination of Brett Giroir to the WHO Executive Board, which has been without a US 
  representative since Trump took office. Of the 34 member states on the Executive Board, the US seat is the only empty 
  one.
  
  Why it matters: Despite complaining of the WHO shortcomings, Trump has not done even the bare minimum to better 
  utilize the WHO as a resource.
  """,
  people=["Trump", "Brett Giroir"],
  orgs=["WHO"],
  sources=[
    Source(
      title="Trump Is Scapegoating the WHO — But Failed to Confirm a U.S. Representative for 3 Years",
      publication="Vice",
      published="2020-04-20",
      url="https://www.vice.com/en_us/article/z3ba5j/trump-is-scapegoating-the-who-but-failed-to-confirm-a-us-representative-for-3-years",
      article_copy="sources/2020-04-20-vice-trump-without-who-representative.pdf",
    ),
  ],
)
