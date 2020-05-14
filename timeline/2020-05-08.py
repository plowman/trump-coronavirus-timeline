from models import Event, Source

TRUMP_PLAYS_DOWN_TESTING = Source(
  title="Trump plays down coronavirus testing as U.S. falls far short of level scientists say is needed",
  publication="The Washington Post",
  published="2020-05-08",
  url="https://www.washingtonpost.com/politics/trump-plays-down-coronavirus-testing-as-us-falls-far-short-of-level-scientists-say-is-needed/2020/05/08/d9241454-913f-11ea-a9c0-73b93422d691_story.html",
  article_copy="sources/2020-05-08-the-washington-post-trump-plays-down-coronavirus-testing-as-us-falls-far-short-of-level-scientists-say-is-needed.pdf",
)

Event(
  date="2020-05-08",
  title="Trump says staff member getting coronavirus is proof more \"testing isn’t necessary.\"",
  description="""
  Since they were testing members of the white house weekly and someone still contracted the virus, the genius 
  conclusion from this is that "testing isn't necessary."
  
  Trump's full quote:
  > “And this is why testing isn’t necessary. We have the best testing in the world, but testing’s not necessarily the 
  answer because they were testing them.”
  """,
  people=["Trump"],
  sources=[
    TRUMP_PLAYS_DOWN_TESTING,
  ],
)

Event(
  date="2020-05-08",
  title="Harvard researchers estimate the US needs to be conducting three times as many tests",
  description="""
  From the article:
  > On Thursday, Harvard University researchers published new estimates, showing that the United States needs to be 
  conducting at least 900,000 tests daily by May 15.
  """,
  sources=[
    TRUMP_PLAYS_DOWN_TESTING,
  ],
)
