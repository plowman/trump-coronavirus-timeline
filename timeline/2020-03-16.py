from models import Event, Source

Event(
  date="2020-03-16",
  title="For ventilators, Trump tells governors 'Try getting it yourselves'",
  description="""
  “Respirators, ventilators, all of the equipment — try getting it yourselves,” he said, adding “We will be backing you,
  but try getting it yourselves. Point of sales, much better, much more direct if you can get it yourself.”

  This is bad because it forces states to bid against one another on ventilators rather than creating a system where 
  there is a single buyer. This is also bad because it does not inspire any confidence that there is a national plan for
  actually getting states the equipment they need.
  """,
  people=["Trump"],
  sources=[
    Source(
      title="Trump to Governors on Ventilators: ‘Try Getting It Yourselves’",
      publication="The New York Times",
      published="2020-03-16",
      url="https://www.nytimes.com/2020/03/16/us/politics/trump-coronavirus-respirators.html",
      article_copy="./sources/2020-03-16-new-york-times-trump-to-governors.pdf",
    ),
  ],
)
