from models import Event, Source

Event(
  date="2020-04-23",
  title="Trump suggests injecting disenfectant might fight coronavirus",
  description="""
  His full quote is impressive even in Trump-adjusted terms:
  > “Supposing we hit the body with a tremendous — whether it’s ultraviolet or just very powerful light. And I think you 
  said that hasn’t been checked, but we’re going to test it? And then I said, supposing you brought the light inside the
  body, either through the skin or some other way.
  
  > And then I see the disinfectant where it knocks it out in a minute — one minute — and is there a way we can do 
  something like that by injection inside, or almost a cleaning? Because you see it gets in the lungs and it does a 
  tremendous number on the lungs, so it would be interesting to check that.”

  Why it matters: Trump just doesn't realize how dumb he is, does he?
  """,
  people=["Trump", "William M. Bryan"],
  sources=[
    Source(
      title="Science Offers Sunlight as Way to Tame Virus, and Trump Rushes Toward It",
      publication="The New York Times",
      published="2020-04-24",
      url="https://www.nytimes.com/2020/04/24/science/sunlight-coronavirus-trump.html",
      article_copy="sources/2020-04-24-new-york-times-trump-injection-disenfectant.pdf",
    ),
  ],
)
