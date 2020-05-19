from models import Event, Source

Event(
  date="2020-05-18",
  title="Trump claims to be taking hydroxychloroquine to protect against coronavirus",
  description="""
  He claims he has been since about around May 8th even though the drug has severe side effects.
  
  As usual we are given the difficult task of choosing between two options:
  1. He is lying to us.
  2. He is really that dumb.
  """,
  people=["Trump"],
  sources=[
    Source(
      title="Trump says he is taking hydroxychloroquine to protect against coronavirus, dismissing safety concerns",
      publication="The Washington Post",
      published="2020-05-18",
      url="https://www.washingtonpost.com/politics/trump-says-he-is-taking-hydroxychloroquine-to-protect-against-coronavirus-dismissing-safety-concerns/2020/05/18/7b8c928a-9946-11ea-ac72-3841fcc9b35f_story.html",
      article_copy="sources/2020-05-18-the-washington-post-trump-says-he-is-taking-hydroxychloroquine-to-protect-against-coronavirus-dismissing-safety-concerns.pdf",
    ),
  ],
)
