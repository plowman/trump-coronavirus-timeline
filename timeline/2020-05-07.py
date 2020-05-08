from models import Event, Source

Event(
  date="2020-05-07",
  title="Trump blocks CDC reopening guidance over fears it will harm the economy",
  description="""
  From the article:
  > White House and other administration officials rejected the recommendations over concerns that they were overly 
  prescriptive, infringed on religious rights and risked further damaging an economy that Mr. Trump was banking on to 
  recover quickly.
  
  Why it matters: It's nice that Trump went through this long process of formally rejecting expert health advice just to
  remind us that he doesn't give a shit.
  """,
  people=["Trump"],
  orgs=["CDC"],
  sources=[
    Source(
      title="White House Blocks C.D.C. Guidance Over Economic and Religious Concerns",
      publication="The New York Times",
      published="2020-05-07",
      url="https://www.nytimes.com/2020/05/07/us/politics/trump-cdc.html",
      article_copy="sources/2020-05-07-the-new-york-times-white-house-blocks-cdc-guidance-over-economic-and-religious-concerns.pdf",
    ),
  ],
)

Event(
  date="2020-05-07",
  title="Trump valet tests positive for coronavirus",
  description="""
  In the continued comedy of errors that is Trump failing to take this seriously until it affects him personally, one of
  the military personal in daily close contact with Trump has tested positive for coronavirus. From the article, "The 
  infected staffer is one of Trump’s personal valets, the military staff members who sometimes serve meals and look 
  after personal needs of the president."
  
  In response he has increased testing from once per week to once per day. 
  
  Why it matters: Trump is not going to take this seriously until he gets it personally, so I guess that's one way this
  could end up being a good thing.
  """,
  people=["Trump"],
  sources=[
    Source(
      title="Trump valet tests positive for coronavirus, sparking fear of West Wing spread",
      publication="The Washington Post",
      published="2020-05-07",
      url="https://www.washingtonpost.com/politics/trump-valet-tests-positive-for-conronavirus-sparking-fear-of-west-wing-spread/2020/05/07/c6b6ce82-9082-11ea-a9c0-73b93422d691_story.html",
      article_copy="sources/2020-05-07-the-washington-post-trump-valet-tests-positive-for-coronavirus-sparking-fear-of-west-wing-spread.pdf",
    ),
  ],
)
