from models import Event, Source

Event(
  date="2020-03-29",
  title="Trump accuses hospitals of stealing masks",
  description="""
  Trump said it doesn't make sense that a hospital would suddenly need way more masks. Instead of learning why you need
  more masks to treat covid patients, he instead amplified a conspiracy theory that the hospitals have been stealing 
  them.

  The quote:
  > Something is going on, and you ought to look into it as reporters. Where are the masks going? Are they going out the
  > back door? How do you go from 10,000 to 300,000? And we have that in a lot of different places.
  """,
  people=["Trump"],
  sources=[
    Source(
      title="Trump could help solve the mask problem. Instead he’s making baseless attacks on New York nurses.",
      publication="Vox",
      published="2020-03-30",
      url="https://www.vox.com/policy-and-politics/2020/3/30/21199538/coronavirus-mask-trump-new-york-hospital-stealing",
      article_copy="./sources/2020-03-30-vox-trump-accuses-hospitals.pdf",
    ),
  ],
)

Event(
  date="2020-03-29",
  title="Trump brags about the ratings of his daily briefings",
  description="""  
  His full tweet is this:
  > Because the “Ratings” of my News Conferences etc. are so high, “Bachelor finale, Monday Night Football type numbers”
    according to the @nytimes, the Lamestream Media is going CRAZY. “Trump is reaching too many people, we must stop 
    him.” said one lunatic. See you at 5:00 P.M.!
  """,
  people=["Trump"],
  sources=[
    Source(
      title="Donald J. Trump on Twitter",
      publication="Twitter",
      published="2020-03-29",
      url="https://twitter.com/realdonaldtrump/status/1244309931874017280",
      article_copy="sources/2020-03-29-twitter-trump-tweet-about-ratings.pdf",
    ),
  ],
)
