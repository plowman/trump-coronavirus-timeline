from models import Event, Source

Event(
  date="2020-04-13",
  title="Trump delays stimulus checks so that his name can appear on them",
  description="""
  Trump has ordered the Treasury department to tell the IRS that his name should appear on the stimulus checks being 
  sent out to Americans. Not only is this not normal, it may actually slow down delivery of the checks by a few days. 

  From the article,
  > The Treasury Department has ordered President Trump’s name be printed on stimulus checks the Internal Revenue 
    Service is rushing to send to tens of millions of Americans, a process that could slow their delivery by a few days,
    senior IRS officials said.
  
  Why it matters: Trump shows that his own vanity is more important than actually getting people the help they need.
  """,
  people=["Trump", ],
  sources=[
    Source(
      title="In unprecedented move, Treasury orders Trump’s name printed on stimulus checks",
      publication="The Washington Post",
      published="2020-04-14",
      url="https://www.washingtonpost.com/politics/coming-to-your-1200-relief-check-donald-j-trumps-name/2020/04/14/071016c2-7e82-11ea-8013-1b6da0e4a2b7_story.html",
      article_copy="sources/2020-04-14-washington-post-trump-signature.pdf",
    ),
  ],
)
