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
