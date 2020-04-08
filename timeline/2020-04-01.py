from models import Event, Source

Event(
  date="2020-04-01",
  title="Trump decides not to open Obamacare markets for enrollment",
  description="""
  Trump has the power to open enrollment in Obamacare so that people without health insurance could get it more easily,
  including those who lost their coverage with their job. He chose not to. No explanation was given.
  """,
  people=["Trump"],
  sources=[
    Source(
      title="Obamacare Markets Will Not Reopen, Trump Decides",
      publication="The New York Times",
      published="2020-04-01",
      url="https://www.nytimes.com/2020/04/01/upshot/obamacare-markets-coronavirus-trump.html",
      article_copy="./sources/2020-04-01-new-york-times-obamacare-markets-will-not-reopen.pdf",
    ),
  ],
)
