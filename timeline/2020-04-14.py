from models import Event, Source

Event(
  date="2020-04-14",
  title="Trump announces he will halt WHO funding",
  description="""
  In an effort to shift blame away from himself, Trump criticized the WHO and said he will halt funding.
  
  “So much death has been caused by their mistakes,” Trump said, repeating the criticisms of his own administration.
  """,
  people=["Trump"],
  orgs=["WHO"],
  sources=[
    Source(
      title="Criticized for Pandemic Response, Trump Tries Shifting Blame to the W.H.O.",
      publication="The New York Times",
      published="2020-04-14",
      url="https://www.nytimes.com/2020/04/14/us/politics/coronavirus-trump-who-funding.html",
      article_copy="sources/2020-04-14-new-york-times-trump-who-funding.pdf",
    ),
  ],
)
