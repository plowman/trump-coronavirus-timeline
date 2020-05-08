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
