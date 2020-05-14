from models import Event, Source

Event(
  date="2020-05-11",
  title="Trump forces everyone at White House to wear a mask, except Trump",
  description="""
  Because Trump doesn't understand that masks would also protect him, he has begun a policy requiring all visitors to 
  the White House to wear masks and excluded himself.
  """,
  people=["Trump"],
  sources=[
    Source(
      title="White House Orders Staff to Wear Masks as Trump Misrepresents Testing Record",
      publication="The New York Times",
      published="2020-05-11",
      url="https://www.nytimes.com/2020/05/11/us/politics/white-house-masks-trump-coronavirus.html",
      article_copy="sources/2020-05-11-the-new-york-times-white-house-orders-staff-to-wear-masks-as-trump-misrepresents-testing-record.pdf",
    ),
  ],
)
