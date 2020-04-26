from models import Event, Source

Event(
  date="2020-04-24",
  title="Trump claims he was being sarcastic with disinfectant comments",
  description="""
  Trump's full quote:
  > “I was asking a question sarcastically to reporters like you. Disinfectant for doing this, maybe on the hands, would 
  work. I was asking… when they use disinfectant it goes away in less than a minute. I was asking a very sarcastic 
  question to reporters in the room about disinfectants on the inside… that was done in a sarcastic way.”
  
  Why it matters: Impressively, the lie is even dumber than the original nonsense. Clearly the hope here is that people
  hear the lie before the truth and can hold onto that sweet sweet particle of deniability.
  """,
  people=["Trump"],
  sources=[
    Source(
      title="Trump claims he was being sarcastic about coronavirus disinfectant comments",
      publication="Fox News",
      published="2020-04-24",
      url="https://www.foxnews.com/politics/trump-claims-he-was-being-sarcastic-about-disinfectant-comments",
      article_copy="sources/2020-04-24-fox-news-trump-claims-he-was-being-sarcastic.pdf",
    ),
  ],
)
