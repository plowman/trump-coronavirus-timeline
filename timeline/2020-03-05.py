from models import Event, Source
from timeline.shared_sources import ECDC_CASES_AND_DEATHS_BY_COUNTRY

Event(
  date="2020-03-05",
  title="US passes 10 deaths",
  description="""
  US has 11 deaths and 159 cases in total.
  """,
  sources=[ECDC_CASES_AND_DEATHS_BY_COUNTRY],
)

Event(
  date="2020-03-05",
  title="Pence says we do not have enough tests to meet demand",
  description="""
  His exact quote is, “We don’t have enough tests today to meet what we anticipate will be the demand going forward.”
  """,
  people=["Pence"],
  sources=[
    Source(
      title="Vice President Mike Pence praises 3M on coronavirus tour",
      publication="Minnesota Star Tribune",
      published="2020-03-05",
      url="https://www.startribune.com/vice-president-mike-pence-visits-3m-on-coronavirus-tour/568524912/",
      article_copy="sources/2020-03-05-star-tribune-pence-3m-tour.pdf",
    ),
  ],
)
