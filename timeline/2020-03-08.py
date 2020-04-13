from models import Event, Source

Event(
  date="2020-03-08",
  title="Trump plays golf",
  description="""
  On March 7th and 8th, Trump played golf. During that time cases in the US would nearly double, from 233 to 433, and
  deaths would increase from 12 to 17.
  """,
  people=["Trump"],
  sources=[
    Source(
      title="Trump Plays Golf While Coronavirus Cases Surge",
      publication="Slate",
      published="2020-03-09",
      url="https://slate.com/news-and-politics/2020/03/trump-plays-golf-coronavirus-cases-surge.html",
      article_copy="sources/2020-03-09-slate-trump-plays-golf.pdf",
    ),
  ],
)
