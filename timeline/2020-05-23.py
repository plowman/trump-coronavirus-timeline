from models import Event, Source

Event(
  date="2020-05-23",
  title="Trump resumes golfing",
  description="""
  He lasted 75 days since he last played, a record for him.
  """,
  people=["Trump"],
  sources=[
    Source(
      title="Trump Plays Golf for 1st Time Since the Coronavirus Pandemic",
      publication="The New York Times",
      published="2020-05-23",
      url="https://www.nytimes.com/aponline/2020/05/23/us/politics/ap-us-virus-outbreak-trump.html",
      article_copy="sources/2020-05-23-the-new-york-times-trump-plays-golf-for-st-time-since-the-coronavirus-pandemic.pdf",
    ),
  ],
)
