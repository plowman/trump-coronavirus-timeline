from models import Event, Source

Event(
  date="2020-04-17",
  title="Trump encourages protests against states deciding what to do on their own",
  description="""
  After releasing formal guidelines that say states get to decide on their own when to open, Trump's next logical step
  was then to encourage protests of states doing exactly that. He doesn't want the blame for opening states early, nor
  does he want the blame for the economy if it's still on the rocks in November, so the best he can do is complain but
  not do anything.
  
  He tweeted, "LIBERATE VIRGINIA, and save your great 2nd Amendment. It is under siege!", "LIBERATE MINNESOTA!", and 
  "LIBERATE MICHIGAN!" while small protests took place in each of those states against stay at home orders. It will not
  surprise you to learn that those three states all have Democratic governors.
  """,
  people=["Trump"],
  sources=[
    Source(
      title="Trump Encourages Protest Against Governors Who Have Imposed Virus Restrictions",
      publication="The New York Times",
      published="2020-04-17",
      url="https://www.nytimes.com/2020/04/17/us/politics/trump-coronavirus-governors.html",
      article_copy="sources/2020-04-17-new-york-times-trump-tweets-to-liberate-states.pdf",
    ),
  ],
)
