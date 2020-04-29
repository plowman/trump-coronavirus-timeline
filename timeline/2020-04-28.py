from models import Event, Source

Event(
  date="2020-04-28",
  title="Trump says he loves Diamond and Silk, who suggested 5G was infecting people with coronavirus",
  description="""
  Trump tweeted, after Fox News dropped them as hosts:
  > "But I love Diamond & Silk, and so do millions of people!"
  
  Some quotes from the duo include:
  > “Is this being deliberately spread? Look, I’m not being a conspiracy theorist, this is real, but I’m asking my own 
  questions. What the hell is going on?"
  
  > "Is this a pandemic, or was it a plandemic? Inquiring minds want to know."
  
  > "So I said that to say this: In each of these places where these hospitals are being built, I want to know how many 
  5G towers are in those places."
  
  Why it matters: Amplifying these people is also amplifying their nonsense. 
  """,
  people=["Trump", "Diamond & Silk"],
  sources=[
    Source(
      title="Fox News Cuts Ties With Diamond & Silk, Unofficial Trump ‘Advisers’ Who Spread Bonkers Coronavirus Claims",
      publication="The Daily Beast",
      published="2020-04-27",
      url="https://www.thedailybeast.com/fox-news-cuts-ties-with-diamond-and-silk",
      article_copy="sources/2020-04-27-daily-beast-fox-news-cuts-ties-with-diamond-and-silk.pdf",
    ),
    Source(
      title="Trump Tweet",
      publication="Twitter",
      published="2020-04-28",
      url="https://twitter.com/realDonaldTrump/status/1255133977360265218",
      article_copy="sources/2020-04-28-twitter-trump-supports-diamond-and-silk.pdf",
    ),
  ],
)
